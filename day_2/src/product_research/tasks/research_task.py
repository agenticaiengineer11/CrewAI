from crewai import Task


def create_research_task(agent) -> Task:
    return Task(
        config="src/product_research/config/tasks.yaml",
        agent=agent,
    )