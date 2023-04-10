#!/usr/bin/env python3

import requests
import openai
import os
import argparse
from dotenv import load_dotenv
from termcolor import colored
from prompts import literature_review_prompt, extract_answer_prompt, keyword_combination_prompt

def auto_researcher(research_question, output_file=None):
    load_dotenv()

    # Set API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    EMAIL = os.getenv("EMAIL", "")
    assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"
    assert EMAIL, "EMAIL environment variable is missing from .env"

    # Configure OpenAI
    openai.api_key = OPENAI_API_KEY

    # Generate keyword combinations for a given research question
    def generate_keyword_combinations(research_question):
        prompt = keyword_combination_prompt.format(research_question=research_question)
        response = openai_call(prompt, use_gpt4=False, temperature=0, max_tokens=200)
        combinations = response.split("\n")
        # Extract keyword combinations and handle cases where there's no colon
        return [combination.split(": ")[1] for combination in combinations if ": " in combination]


    # Fetch papers from Semantic Scholar API
    def fetch_papers(search_query, limit=100, year_range=None):
        base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": search_query,
            "limit": limit,
            "fields": "title,url,abstract,authors,citationStyles,journal,citationCount,year,externalIds"
        }

        if year_range is not None:
            params["year"] = year_range

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        else:
            raise Exception(f"Failed to fetch data from Semantic Scholar API: {response.status_code}")


    # Fetch and sort papers by citation count
    # If you don't want to limit the year range, set year_range to None
    def fetch_and_sort_papers(search_query, limit=100, top_n=20, year_range="2010-2023", keyword_combinations=None):
        papers = []
        if keyword_combinations is None:
            keyword_combinations = [search_query]

        for combination in keyword_combinations:
            papers.extend(fetch_papers(combination, limit, year_range))

        sorted_papers = sorted(papers, key=lambda x: x['citationCount'], reverse=True)
        return sorted_papers[:top_n]


    # Call OpenAI API with a given prompt (GPT-3.5 turbo or GPT-4)
    def openai_call(prompt: str, use_gpt4: bool = False, temperature: float = 0.5, max_tokens: int = 100):
        if not use_gpt4:
            #Call GPT-3.5 turbo model
            messages=[{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content.strip()
        else:
            #Call GPT-4 chat model
            messages=[{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages = messages,
                temperature=temperature,
                max_tokens=max_tokens,
                n=1,
                stop=None,
            )
            return response.choices[0].message.content.strip()


    # Extract answers from papers using OpenAI API
    def extract_answers_from_papers(papers, research_question, use_gpt4=False, temperature=0.1, max_tokens=150):
        answers = []
        default_answer = "No answer found."

        for paper in papers:
            abstract = paper.get("abstract", "")
            title = colored(paper.get("title", ""), "magenta", attrs=["bold"])
            if "externalIds" in paper and "DOI" in paper["externalIds"]:
                citation = get_citation_by_doi(paper["externalIds"]["DOI"])
            else:
                citation = paper["url"]
            prompt = extract_answer_prompt.format(research_question=research_question, abstract=abstract)
            answer = openai_call(prompt, use_gpt4=use_gpt4, temperature=temperature, max_tokens=max_tokens)

            print(f"Processing paper: {title}")

            answer_with_citation = f"{answer}\n{citation}"
            if answer != default_answer:
                answer_with_citation = f"{answer} SOURCE: {citation}"
                answers.append(answer_with_citation)
                print(colored(f"Answer found!", "green"))
                print(colored(f"{answer_with_citation}", "cyan"))

        return answers

    # Get APA citation for a paper using DOI
    def get_citation_by_doi(doi):
        url = f"https://api.citeas.org/product/{doi}?email={EMAIL}"
        response = requests.get(url)
        data = response.json()
        return data["citations"][0]["citation"]

    # Combine answers into a concise literature review using OpenAI API
    def combine_answers(answers, research_question, use_gpt4=False, temperature=0.1, max_tokens=1800):
        answer_list = "\n\n".join(answers)
        prompt = literature_review_prompt.format(research_question=research_question, answer_list=answer_list)
        literature_review = openai_call(prompt, use_gpt4=use_gpt4, temperature=temperature, max_tokens=max_tokens)

        return literature_review

    # Extract bibliographical citations from answers
    def extract_citations(answers):
        citations = []
        for answer in answers:
            citation_start = answer.rfind("SOURCE: ")
            if citation_start != -1:
                citation = answer[citation_start + len("SOURCE: "):]
                citations.append(citation)
        return citations

    print(colored(f"Research question: {research_question}", "yellow", attrs=["bold", "blink"]))
    print(colored("Auto Researcher initiated!", "yellow"))

    # Generate keyword combinations
    print(colored("Generating keyword combinations...", "yellow"))
    keyword_combinations = generate_keyword_combinations(research_question)
    print(colored("Keyword combinations generated!", "green"))

    # Fetch the top 20 papers for the research question
    search_query = research_question
    print(colored("Fetching top 20 papers...", "yellow"))
    top_papers = fetch_and_sort_papers(search_query, keyword_combinations=keyword_combinations)
    print(colored("Top 20 papers fetched!", "green"))

    # Extract answers and from the top 20 papers
    print(colored("Extracting research findings from papers...", "yellow"))
    answers = extract_answers_from_papers(top_papers, research_question)
    print(colored("Research findings extracted!", "green"))

    # Combine answers into a concise academic literature review
    print(colored("Synthesizing answers...", "yellow"))
    literature_review = combine_answers(answers, research_question)
    print(colored("Literature review generated!", "green"))

    # Extract citations from answers and append a references list to the literature review
    citations = extract_citations(answers)
    references_list = "\n".join([f"{idx + 1}. {citation}" for idx, citation in enumerate(citations)])
    literature_review += "\n\nReferences:\n" + references_list

    # Append the keyword combinations to the literature review
    literature_review += "\n\nKeyword combinations used to search for papers: "
    literature_review += ", ".join([f"{i+1}. {combination}" for i, combination in enumerate(keyword_combinations)])

    # Print the academic literature review
    print(colored("Academic Literature Review:", "cyan"), literature_review, "\n")

    return literature_review

if __name__ == "__main__":
    import sys
    parser = argparse.ArgumentParser(description="Auto Researcher")
    parser.add_argument("-o", "--output", dest="output_file", help="File to save the literature review", default=None)
    parser.add_argument("-q", "--question", dest="research_question", help="The research question you want to investigate", default=None)
    args = parser.parse_args()
    
    default_question = "How to make good Espresso?"
    research_question = args.research_question if args.research_question else default_question

    auto_researcher(research_question, args.output_file)
