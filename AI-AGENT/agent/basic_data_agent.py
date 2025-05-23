
import pandas as pd
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_csv_agent


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def create_agent(csv_path):
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=api_key),
        csv_path,
        verbose=True
    )
    return agent

def run_query(agent, query):
    return agent.run(query)


