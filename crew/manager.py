from crewai import Crew, Process
from crew.agents import assessment, nutriagent, workout_planner

class FitnessCrewManager:
    def __init__(self):
        # Initialize agents
        self.ass_agent = assessment.AssessmentAgent()
        self.nutri = nutriagent.NutritionAgent()
        self.workout = workout_planner.WorkoutPlanner()
        
        # Create crew
        self.crew = Crew(
            name='fitness_crew',
            agents=[self.ass_agent.agent, self.workout.agent, self.nutri.agent],
            tasks=[self.ass_agent.task, self.workout.task, self.nutri.task],
            cache=True,
            process=Process.sequential,
            verbose=True,
            memory=False
        )
    
    def process_user_request(self, user_input: str):
        """Process user request and return the result"""
        try:
            print("🔄 Running AI agents...")
            result = self.crew.kickoff({"input": user_input})

            # Extract individual results
            assessment_result = str(result.tasks_output[0]) if len(result.tasks_output) > 0 else ""
            workout_result = str(result.tasks_output[1]) if len(result.tasks_output) > 1 else ""
            nutrition_result = str(result.tasks_output[2]) if len(result.tasks_output) > 2 else ""

            print("✅ All agents completed successfully!")

            return {
                "success": True,
                "assessment": assessment_result,
                "workout_plan": workout_result,
                "nutrition_plan": nutrition_result
            }
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }