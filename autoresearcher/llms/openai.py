import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"

# Configure OpenAI
openai.api_key = OPENAI_API_KEY


def openai_call(
    prompt: str, use_gpt4: bool = False, temperature: float = 0.5, max_tokens: int = 100
):
    """
    Calls OpenAI API to generate a response to a given prompt.
    Args:
      prompt (str): The prompt to generate a response to.
      use_gpt4 (bool, optional): Whether to use GPT-4o-mini or GPT-4o. Defaults to False.
      temperature (float, optional): The temperature of the response. Defaults to 0.5.
      max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 100.
    Returns:
      str: The generated response.
    Examples:
      >>> openai_call("Hello, how are you?")
      "I'm doing great, thanks for asking!"
    Notes:
      The OpenAI API key must be set in the environment variable OPENAI_API_KEY.
    """
    if not use_gpt4:
        # Call GPT-4o-mini model
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].message.content.strip()
    else:
        # Call GPT-4o model
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=None,
        )
        return response.choices[0].message.content.strip()
