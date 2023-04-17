from autoresearcher.llms.openai import openai_call
from autoresearcher.utils.prompts import keyword_combination_prompt


# Generate keyword combinations for a given research question
def generate_keyword_combinations(research_question):
    """
    Generates keyword combinations for a given research question.
    Args:
      research_question (str): The research question to generate keyword combinations for.
    Returns:
      list: A list of keyword combinations for the given research question.
    Examples:
      >>> generate_keyword_combinations("What is the impact of AI on healthcare?")
      ["AI healthcare", "impact AI healthcare", "AI healthcare impact"]
    """
    prompt = keyword_combination_prompt.format(research_question=research_question)
    response = openai_call(prompt, use_gpt4=False, temperature=0, max_tokens=200)
    combinations = response.split("\n")
    return [
        combination.split(": ")[1]
        for combination in combinations
        if ": " in combination
    ]
