import os
import argparse

os.environ["OPENAI_API_KEY"] = "<your_openai_api_key>"
os.environ["EMAIL"] = "<your_email>"

from autoresearcher import literature_review

parser = argparse.ArgumentParser()
parser.add_argument("--research_question", type=str, default="What is the meaning of life?")
parser.add_argument("--output_file", type=str, default="literature_review.txt")
args = parser.parse_args()

with open(args.output_file, "a") as f:
    f.write(f"Research question: {args.research_question}\n\n")

with open(args.output_file, "a") as f:
    f.write(literature_review(args.research_question))
