from crewai import Agent  

research_agent = Agent(
    role="Product Research Specialist",
    goal="Research products and identify useful market information.",
    backstory=(
        "You are an experienced product research specialist "
        "who analyzes products and their potential markets."
    ),
)

print(research_agent)