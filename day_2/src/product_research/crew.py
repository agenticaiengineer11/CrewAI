import crewai.llms.cache as _crewai_cache

from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()

_crewai_cache.mark_cache_breakpoint = lambda msg: msg


@CrewBase
class ProductResearchCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        temperature=0.7,
    )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            llm=self.llm,
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )