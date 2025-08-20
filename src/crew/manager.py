from crewai import Crew, Process
from src.crew.agents import assessment, nutriagent, workout_planner

ass_agent = assessment.AssessmentAgent()
nutri = nutriagent.NutritionAgent()
workout = workout_planner.WorkoutPlanner()

crew = Crew(
    name='manager',
    agents=[ass_agent.agent, nutri.agent, workout.agent],
    tasks=[ass_agent.task, nutri.task, workout.task],
    cache=True,
    process=Process.sequential,
    verbose=True,
    memory=True
)

if __name__ == "__main__":
    crew.kickoff({"input": "I'm a 20 year old male weighing 74kgs, need to lose some weight and gain muscles, help me out."})