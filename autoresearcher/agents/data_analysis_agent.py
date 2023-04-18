from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"


class DataAnalysisAgent:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)
        self.agent = create_pandas_dataframe_agent(OpenAI(temperature=0), self.df, verbose=True)

    def run(self, command):
        return self.agent.run(command)