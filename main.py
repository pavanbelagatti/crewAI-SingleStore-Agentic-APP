import warnings
import asyncio

# --- Suppress Deprecation Warnings globally ---
warnings.simplefilter("ignore", category=DeprecationWarning)

# --- Ensure an event loop exists (avoids asyncio warning on Python 3.12) ---
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from crewai import Agent, Task, Crew
from crewai_tools import SingleStoreSearchTool
from config import SINGLESTORE_CONFIG


def run_agentic_app(query: str):
    """Run a CrewAI agentic workflow with SingleStoreSearchTool for a given query."""

    # 1. Setup Tool
    tool = SingleStoreSearchTool(
        tables=["products"],  # restrict to 'products' table; ensure it exists in DB
        host=SINGLESTORE_CONFIG["host"],
        user=SINGLESTORE_CONFIG["user"],
        password=SINGLESTORE_CONFIG["password"],
        database=SINGLESTORE_CONFIG["database"],
    )

    # 2. Setup Agent
    agent = Agent(
        role="Analyst",
        goal=f"Answer the question: {query}",
        backstory=(
            "A data analyst who knows how to write SQL and retrieve insights "
            "from SingleStore in a safe and optimized way."
        ),
        tools=[tool],
        llm="gpt-4o-mini",  # can be changed to gpt-4, gpt-3.5-turbo, etc.
        verbose=True,
    )

    # 3. Setup Task
    task = Task(
        description=query,
        expected_output="Return results in JSON or a clean, tabular summary",
        agent=agent,
    )

    # 4. Setup Crew
    crew = Crew(agents=[agent], tasks=[task], verbose=True)

    # 5. Kick off and return result
    return crew.kickoff()


if __name__ == "__main__":
    print("\n🔎 Product Insights Agent (CrewAI + SingleStore)")
    print("--------------------------------------------------")
    user_query = input("Ask me anything about products: ")

    result = run_agentic_app(user_query)

    print("\n=== Result ===")
    print(result)
    print("\n✅ Query complete!")