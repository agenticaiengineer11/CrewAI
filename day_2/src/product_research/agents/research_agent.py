import crewai.llms.cache as _crewai_cache

from crewai import Agent, LLM
_crewai_cache.mark_cache_breakpoint = lambda msg: msg


model = LLM(
    model="groq/openai/gpt-oss-120b",
    temperature=0.7,
)


def create_research_agent() -> Agent:
    return Agent(
        role="Product Research Specialist",
        goal="Research products and identify useful market information.",
        backstory=(
            "You are an experienced product research specialist "
            "who analyzes products and their potential markets."
        ),
        llm=model,
    )