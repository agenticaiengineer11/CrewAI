from crewai import Task

from product_research.agents.research_agent import create_research_agent


def create_research_task() -> Task:
    research_agent = create_research_agent()

    return Task(
        description=(
            "Research the product '{product_name}'. "
            "Identify its main features, target customers, "
            "common use cases, and important market considerations."
        ),
        expected_output=(
            "A structured product research report containing:\n"
            "1. Product overview\n"
            "2. Main features\n"
            "3. Target customers\n"
            "4. Common use cases\n"
            "5. Market considerations"
        ),
        agent=research_agent,
    )