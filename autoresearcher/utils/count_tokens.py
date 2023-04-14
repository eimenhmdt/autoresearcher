import tiktoken

def count_tokens(text):
    # encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("gpt-4")

    tokens = encoding.encode(text)
    return len(tokens)
