import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults

from config import api_key # Import api_key from config.py

load_dotenv()

# 🔹 OpenRouter LLM Setup
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key, # Use the directly available api_key variable
    model="stepfun/step-3.5-flash:free",  # or any free model
    temperature=0
)

# 🔹 Free Search Tool
search_tool = DuckDuckGoSearchResults()
