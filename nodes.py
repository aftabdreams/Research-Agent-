from typing import List

from models import ResearchState
from tools import llm, search_tool

def planner(state: ResearchState):
    prompt = f"""
    Break this topic into 5 deep research sub-questions.
    Topic: {state['topic']}
    Return as numbered list.
    """

    response = llm.invoke(prompt)

    subtopics = [
        line.strip() for line in response.content.split("\n")
        if line.strip()
    ]

    return {"subtopics": subtopics}

def searcher(state: ResearchState):
    results = []

    for sub in state["subtopics"]:
        query = f"{sub} statistics examples expert analysis"
        search_output = search_tool.run(query)

        results.append(f"Search Query: {sub}\n{search_output}\n")

    return {"search_results": results}

def researcher(state: ResearchState):
    combined_data = "\n\n".join(state["search_results"])

    prompt = f"""
    Analyze the following research data deeply.

    Extract:
    - Key insights
    - Important statistics
    - Case studies
    - Trends
    - Expert opinions

    Organize clearly.

    Data:
    {combined_data}
    """

    response = llm.invoke(prompt)

    return {"research_notes": response.content}

def writer(state: ResearchState):
    prompt = f"""
    Write a detailed professional research report (1500+ words).

    Include:
    - Title
    - Executive Summary
    - Detailed Sections
    - Case Studies
    - Data Analysis
    - Conclusion

    Based on:
    {state['research_notes']}
    """

    response = llm.invoke(prompt)

    return {"final_report": response.content}
