from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv
from termcolor import colored
from autoresearcher.data_sources.file_loaders.pdf_loader import load_pdf
from autoresearcher.utils.analyze_section import analyze_section

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"

def analyze_paper(pdf_path):
    print(
        colored(
            f"Paper analysis initiated", "yellow", attrs=["bold", "blink"]
        )
    )
    pages = load_pdf(pdf_path)

    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())

    findings = analyze_section(faiss_index, "findings", "Conclusion, findings, results")
    methodology = analyze_section(faiss_index, "methodology", "Methodology")
    limitations = analyze_section(faiss_index, "limitations", "Limitations")

    merged_findings = (
        f"{colored('Main findings:', 'green')} {findings}\n"
        f"{colored('Methodology:', 'yellow')} {methodology}\n"
        f"{colored('Limitations:', 'red')} {limitations}"
    )

    print("\n" + colored("Analysis results:", "magenta", attrs=["bold"]))
    print(merged_findings)