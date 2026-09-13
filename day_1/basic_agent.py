import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from crewai import Agent, Task, Crew, LLM

model = LLM(
    model="groq/openai/gpt-oss-120b",
    temperature=0.7,
)

research_agent = Agent(
    role="Product Research Specialist",
    goal="Research products and identify useful market information.",
    backstory=(
        "You are an experienced product research specialist "
        "who analyzes products and their potential markets."
    ),
    llm=model,
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

result = research_crew.kickoff()

print(result)