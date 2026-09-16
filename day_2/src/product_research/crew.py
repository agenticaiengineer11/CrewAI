from crewai import Crew, Process

from product_research.agents.research_agent import create_research_agent
from product_research.tasks.research_task import create_research_task


def create_crew() -> Crew:
    research_agent = create_research_agent()
    research_task = create_research_task()

    return Crew(
        agents=[research_agent],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True
    )