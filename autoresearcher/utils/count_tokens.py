import tiktoken


def count_tokens(text):
    """
    Counts the number of tokens in a given text.
    Args:
      text (str): The text to tokenize.
    Returns:
      int: The number of tokens in `text`.
    Examples:
      >>> count_tokens("This is a sentence.")
      6
    Notes:
      The encoding used is determined by the `tiktoken.encoding_for_model` function.
    """
    # encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("gpt-4")

    tokens = encoding.encode(text)
    return len(tokens)
