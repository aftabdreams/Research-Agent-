from typing import TypedDict, List

class ResearchState(TypedDict):
    topic: str
    subtopics: List[str]
    search_results: List[str]
    research_notes: str
    final_report: str
