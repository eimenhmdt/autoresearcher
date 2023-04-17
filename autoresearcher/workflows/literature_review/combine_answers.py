from autoresearcher.llms.openai import openai_call
from autoresearcher.utils.prompts import literature_review_prompt
from autoresearcher.utils.count_tokens import count_tokens


# Combine answers into a concise literature review using OpenAI API
def combine_answers(answers, research_question, use_gpt4=False, temperature=0.1):
    """
    Combines a list of answers into a concise literature review using OpenAI API.
    Args:
      answers (list): A list of answers to combine.
      research_question (str): The research question to use in the literature review.
      use_gpt4 (bool, optional): Whether to use GPT-4 for the literature review. Defaults to False.
      temperature (float, optional): The temperature to use for the OpenAI API. Defaults to 0.1.
    Returns:
      str: The literature review.
    Examples:
      >>> answers = ["Answer 1", "Answer 2"]
      >>> research_question = "What is the impact of AI on society?"
      >>> combine_answers(answers, research_question)
      "The impact of AI on society is significant. Answer 1...Answer 2..."
    """
    answer_list = "\n\n".join(answers)
    prompt = literature_review_prompt.format(
        research_question=research_question, answer_list=answer_list
    )

    # Calculate the tokens in the input
    input_tokens = count_tokens(prompt)

    # Calculate the remaining tokens for the response
    remaining_tokens = 4080 - input_tokens
    max_tokens = max(remaining_tokens, 0)
    literature_review = openai_call(
        prompt, use_gpt4=use_gpt4, temperature=temperature, max_tokens=max_tokens
    )

    return literature_review
