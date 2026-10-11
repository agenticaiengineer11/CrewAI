from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

load_dotenv()


@CrewBase
class CodeReviewerCrew:
    """Two agents for AI code review."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def code_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_analyzer"],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_reviewer"],
            verbose=True,
            allow_delegation=False,
        )

    @task
    def analyze_code(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_code"],
        )

    @task
    def review_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_code"],
            context=[self.analyze_code()],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


if __name__ == "__main__":
    sample_code = """
def divide(a, b):
    return a / b

def get_user(users, index):
    return users[index]
"""

    result = CodeReviewerCrew().crew().kickoff(
        inputs={"code": sample_code}
    )

    print("\n===== FINAL CODE REVIEW =====\n")
    print(result)