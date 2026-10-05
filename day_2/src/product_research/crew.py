import crewai.llms.cache as _crewai_cache
from product_research.tools.ecommerce_tool import calculate_profit_margin
from product_research.tools.product_price_tool import calculate_product_price
from product_research.tools.product_review_tool import calculate_product_review_sentiment
from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()

# Compatibility workaround for the current Groq setup
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
    def manager(self) ->Agent:
        return Agent(
            config = self.agents_config["manager"],
            llm =self.llm,
            verbose = True,
            allow_delegation = True,
            max_iter = 5,

        )
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            llm=self.llm,
            verbose=True,
            tools = [calculate_profit_margin, calculate_product_price, calculate_product_review_sentiment],
            allow_delegation=False,
            max_iter=5,
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_analyst"],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
        )

    @agent
    def market_research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_analyst"],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(),
        )

    @task
    def competitor_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitor_task"],
            agent=self.competitor_analyst(),
            context=[self.research_task()],
        )
    @task
    def market_summary_task(self) -> Task:
        return Task(
            config = self.tasks_config["market_summary_task"],
            agent = self.market_research_analyst(),
            context = [self.research_task(), self.competitor_task()],
        )
    

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.manager(),
            memory= True,
            verbose=True,
    )