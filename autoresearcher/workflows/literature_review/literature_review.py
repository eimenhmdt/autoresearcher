#!/usr/bin/env python3
from termcolor import colored
from autoresearcher.llms.openai import openai_call
from autoresearcher.utils.get_citations import get_citation_by_doi
from autoresearcher.utils.prompts import literature_review_prompt, extract_answer_prompt, keyword_combination_prompt
from autoresearcher.data_sources.web_apis.semantic_scholar_loader import SemanticScholarLoader

def literature_review(research_question, output_file=None):

    SemanticScholar = SemanticScholarLoader()

    # Generate keyword combinations for a given research question
    def generate_keyword_combinations(research_question):
        prompt = keyword_combination_prompt.format(research_question=research_question)
        response = openai_call(prompt, use_gpt4=False, temperature=0, max_tokens=200)
        combinations = response.split("\n")
        # Extract keyword combinations and handle cases where there's no colon
        return [combination.split(": ")[1] for combination in combinations if ": " in combination]

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
    top_papers = SemanticScholar.fetch_and_sort_papers(search_query, keyword_combinations=keyword_combinations, year_range="2000-2023")
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

    # Save the literature review to a file if the output_file argument is provided
    if output_file:
        with open(output_file, 'w') as f:
            f.write(literature_review)
        print(colored(f"Literature review saved to {output_file}", "green"))

    return literature_review

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        research_question = sys.argv[1]
        output_file = sys.argv[2]
    elif len(sys.argv) > 1:
        research_question = sys.argv[1]
        output_file = None
    else:
        raise ValueError("No research question provided.")

    literature_review(research_question, output_file)