#!/usr/bin/env python3
from termcolor import colored
from autoresearcher.llms.openai import openai_call
from autoresearcher.workflows.literature_review.extract_citations import (
    extract_citations,
)
from autoresearcher.utils.generate_keyword_combinations import (
    generate_keyword_combinations,
)
from autoresearcher.workflows.literature_review.combine_answers import combine_answers
from autoresearcher.workflows.literature_review.extract_answers_from_papers import (
    extract_answers_from_papers,
)
from autoresearcher.data_sources.web_apis.semantic_scholar_loader import (
    SemanticScholarLoader,
)


def literature_review(research_question, output_file=None, use_gpt4=False):
    """
    Generates an academic literature review for a given research question.
    Args:
      research_question (str): The research question to generate a literature review for.
      output_file (str, optional): The file path to save the literature review to.
      use_gpt4 (bool, optional): Whether to use GPT-4 for generating the literature review. Defaults to False.
    Returns:
      str: The generated literature review.
    Examples:
      >>> literature_review('What is the impact of AI on healthcare?')
      Research question: What is the impact of AI on healthcare?
      Auto Researcher initiated!
      Generating keyword combinations...
      Keyword combinations generated!
      Fetching top 20 papers...
      Top 20 papers fetched!
      Extracting research findings from papers...
      Research findings extracted!
      Synthesizing answers...
      Literature review generated!
      Academic Literature Review: ...
      References:
      1. ...
      Keyword combinations used to search for papers: 1. AI healthcare, 2. impact AI healthcare
    """
    SemanticScholar = SemanticScholarLoader()

    print(
        colored(
            f"Research question: {research_question}", "yellow", attrs=["bold", "blink"]
        )
    )
    print(colored("Auto Researcher initiated!", "yellow"))

    # Generate keyword combinations
    print(colored("Generating keyword combinations...", "yellow"))
    keyword_combinations = generate_keyword_combinations(research_question)
    print(colored("Keyword combinations generated!", "green"))

    # Fetch the top 20 papers for the research question
    search_query = research_question
    print(colored("Fetching top 20 papers...", "yellow"))
    top_papers = SemanticScholar.fetch_and_sort_papers(
        search_query, keyword_combinations=keyword_combinations, year_range="2000-2023"
    )
    print(colored("Top 20 papers fetched!", "green"))

    # Extract answers and from the top 20 papers
    print(colored("Extracting research findings from papers...", "yellow"))
    answers = extract_answers_from_papers(top_papers, research_question, use_gpt4=use_gpt4)
    print(colored("Research findings extracted!", "green"))

    # Combine answers into a concise academic literature review
    print(colored("Synthesizing answers...", "yellow"))
    literature_review = combine_answers(answers, research_question, use_gpt4=use_gpt4)
    print(colored("Literature review generated!", "green"))

    # Extract citations from answers and append a references list to the literature review
    citations = extract_citations(answers)
    references_list = "\n".join(
        [f"{idx + 1}. {citation}" for idx, citation in enumerate(citations)]
    )
    literature_review += "\n\nReferences:\n" + references_list

    # Append the keyword combinations to the literature review
    literature_review += "\n\nKeyword combinations used to search for papers: "
    literature_review += ", ".join(
        [f"{i+1}. {combination}" for i, combination in enumerate(keyword_combinations)]
    )

    # Print the academic literature review
    print(colored("Academic Literature Review:", "cyan"), literature_review, "\n")

    # Save the literature review to a file if the output_file argument is provided
    if output_file:
        with open(output_file, "w") as f:
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
        raise ValueError(
            "No research question provided. Usage: python literature_review.py 'My research question' 'optional_output_file.txt'"
        )

    literature_review(research_question, output_file)
