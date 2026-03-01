import asyncio

from langgraph.graph import StateGraph, END

from models import ResearchState
from nodes import planner, searcher, researcher, writer
from utils import generate_pdf

# Define the topic for research
topic = "secret strategies of the ultra successful to become highly successful by hook or by crook , give all there secrets how they optimise each and every thing "

# Build the Langgraph graph
builder = StateGraph(ResearchState)

builder.add_node("planner", planner)
builder.add_node("searcher", searcher)
builder.add_node("researcher", researcher)
builder.add_node("writer", writer)

builder.set_entry_point("planner")

builder.add_edge("planner", "searcher")
builder.add_edge("searcher", "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", END)

graph = builder.compile()

async def run_graph_async():
    return await graph.ainvoke({"topic": topic})

# Run the graph and generate the PDF
if __name__ == "__main__":
    result = asyncio.run(run_graph_async())
    generate_pdf(result["final_report"])
    print("PDF generated successfully!")
