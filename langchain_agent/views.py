from django.shortcuts import render

# Create your views here.

from langchain.agents import initialize_agent
from langchain.tools import Tool

def process_query(query):
    # Add logic for LangChain Agent
    return f"Response for: {query}"
