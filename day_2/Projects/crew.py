from crewai import Agent,Process, Task, Crew
from crewai.project import CrewBase, agent, task , crew
@CrewBase
class CodeReviewerCrew:
    """Two agents for AI code Review"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def code_analyzer(self)->Agent:
        return Agent(
            config =self.agents_config["code_analyzer"],
            verbose =True,
            allow_delegation = False,
        )
    @agent
    def code_reviewer(self)->Agent:
        return Agent(
            config = self.agents_config["code_reviewer"],
            verbose = True,
            allow_delegation = False,

        )
    @task
    def analyze_code(self)->Task:
        return Task(
            config =self.tasks_config["analyze_code"],

        )
    @task
    def review_code(self)->Task:
        return Task(
            config =self.tasks_config["review_code"],
            
        )