from crewai import Agent, Task, Crew

research_agent = Agent(
    role="Product Research Specialist",
    goal="Research products and identify useful market information.",
    backstory=(
        "You are an experienced product research specialist "
        "who analyzes products and their potential markets."
    ),
)

research_task = Task(
    description=(
        "Research the wireless charging station market. "
        "Identify the main product features, target customers, "
        "common use cases, and major market opportunities."
    ),
    expected_output=(
        "A structured market research report covering "
        "product features, target customers, use cases, "
        "and market opportunities."
    ),
    agent=research_agent,
)

research_crew = Crew(
    agents=[research_agent],
    tasks=[research_task],
)

print(research_crew)