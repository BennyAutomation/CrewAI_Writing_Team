from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from writerideamachine.tools.file_writer import SaveToFileTool

save_tool = SaveToFileTool()

@CrewBase
class Writerideamachine():
    """Writerideamachine crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def brainstormer(self) -> Agent:
        return Agent(
            config=self.agents_config['brainstormer'],
            verbose=True
        )

    @agent
    def research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analyst'],
            verbose=True
        )
    
    @agent
    def copyright_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['copyright_specialist'],
            verbose=True
        )
    
    @agent
    def publisher(self) -> Agent:
        return Agent(
            config=self.agents_config['publisher'],
            verbose=True
        )
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )
    
    @agent
    def proofreader(self) -> Agent:
        return Agent(
            config=self.agents_config['proofreader'],
            tools=[save_tool],
            verbose=True
        )

    @task
    def brainstorming_task(self) -> Task:
        return Task(
            config=self.tasks_config['brainstorming_task'],
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            output_file='report.md'
        )
    
    @task
    def copyrighting_task(self) -> Task:
        return Task(
            config=self.tasks_config['copyrighting_task'],
            output_file='report.md'
        )
    
    @task
    def publishing_task(self) -> Task:
        return Task(
            config=self.tasks_config['publishing_task'],
            output_file='report.md'
        )
    
    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            output_file='report.md'
        )
    
    @task
    def proofreading_task(self) -> Task:
        return Task(
            config=self.tasks_config['proofreading_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Writerideamachine crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
