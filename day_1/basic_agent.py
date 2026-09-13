from crewai import Agent, Task

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

print(research_task)