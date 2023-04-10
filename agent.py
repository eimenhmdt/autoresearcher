#!/usr/bin/env python3
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Set API Keys

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


llm = OpenAI(temperature=0)

tools = load_tools(["llm-math", "python_repl"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("Write and execute a python script that asks the user to input his name and then creates a joke including that name?")