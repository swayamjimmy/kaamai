from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class JobResearchCrew():
    """Job Research Crew for company intelligence and application preparation"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def role_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['role_analyst'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['report_writer'],  # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']  # type: ignore[index]
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task']  # type: ignore[index]
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task']  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Job Research Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )