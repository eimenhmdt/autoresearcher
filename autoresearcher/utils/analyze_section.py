from autoresearcher.llms.openai import openai_call
from termcolor import colored


def analyze_section(faiss_index, section_name, search_term, k=1):
    print(colored(f"Analyzing {section_name}...", "cyan"))
    docs = faiss_index.similarity_search(search_term, k=k)

    context = ""
    for doc in docs:
        formatted_string = str(doc)
        context += formatted_string + "\n"

    prompt = f"What are the main {section_name} in the paper:" + context

    result = openai_call(prompt, use_gpt4=False, temperature=0, max_tokens=500)

    return result