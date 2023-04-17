#!/usr/bin/env python3
from autoresearcher.utils.get_citations import get_citation_by_doi
from termcolor import colored
from autoresearcher.utils.prompts import extract_answer_prompt
from autoresearcher.llms.openai import openai_call


# Extract answers from paper abstracts
def extract_answers_from_papers(
    papers, research_question, use_gpt4=False, temperature=0, max_tokens=150
):
    """
    Extracts answers from paper abstracts.
    Args:
      papers (list): A list of papers.
      research_question (str): The research question to answer.
      use_gpt4 (bool, optional): Whether to use GPT-4 for answer extraction. Defaults to False.
      temperature (float, optional): The temperature for GPT-4 answer extraction. Defaults to 0.
      max_tokens (int, optional): The maximum number of tokens for GPT-4 answer extraction. Defaults to 150.
    Returns:
      list: A list of answers extracted from the paper abstracts.
    Examples:
      >>> extract_answers_from_papers(papers, research_question)
      ['Answer 1 SOURCE: Citation 1', 'Answer 2 SOURCE: Citation 2']
    """
    answers = []
    default_answer = "No answer found."

    for paper in papers:
        abstract = paper.get("abstract", "")
        title = colored(paper.get("title", ""), "magenta", attrs=["bold"])
        if "externalIds" in paper and "DOI" in paper["externalIds"]:
            citation = get_citation_by_doi(paper["externalIds"]["DOI"])
        else:
            citation = paper["url"]
        prompt = extract_answer_prompt.format(
            research_question=research_question, abstract=abstract
        )
        answer = openai_call(
            prompt, use_gpt4=use_gpt4, temperature=temperature, max_tokens=max_tokens
        )

        print(f"Processing paper: {title}")

        answer_with_citation = f"{answer}\n{citation}"
        if answer != default_answer:
            answer_with_citation = f"{answer} SOURCE: {citation}"
            answers.append(answer_with_citation)
            print(colored(f"Answer found!", "green"))
            print(colored(f"{answer_with_citation}", "cyan"))

    return answers
