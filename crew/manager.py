from crewai import Crew, Process
from crew.agents import assessment, nutriagent, workout_planner
from crew.database_manager import DatabaseManager
from db.database import create_tables

class FitnessCrewManager:
    def __init__(self, local_only: bool = False):
        self.local_only = local_only
        # Ensure database tables exist when not in local-only mode
        if not self.local_only:
            create_tables()
        
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
        """Main method to process user request. When local_only, skips database."""
        # Run the crew first
        print("🔄 Running AI agents...")
        result = self.crew.kickoff({"input": user_input})

        # Extract individual results
        assessment_result = str(result.tasks_output[0]) if len(result.tasks_output) > 0 else ""
        workout_result = str(result.tasks_output[1]) if len(result.tasks_output) > 1 else ""
        nutrition_result = str(result.tasks_output[2]) if len(result.tasks_output) > 2 else ""

        if self.local_only:
            # Local-only: do not touch DB
            return {
                "success": True,
                "user_id": None,
                "assessment_id": None,
                "workout_id": None,
                "nutrition_id": None,
                "assessment": assessment_result,
                "workout_plan": workout_result,
                "nutrition_plan": nutrition_result
            }

        # DB-backed flow
        db_manager = DatabaseManager()
        try:
            user_id = db_manager.create_user_session(user_input)
            print(f"✅ Created user session with ID: {user_id}")

            print("💾 Saving results to database...")
            assessment_record = db_manager.save_assessment(user_id, assessment_result)
            workout_record = db_manager.save_workout_plan(user_id, workout_result)
            nutrition_record = db_manager.save_nutrition_plan(user_id, nutrition_result)

            print("✅ All data saved successfully!")

            return {
                "success": True,
                "user_id": user_id,
                "assessment_id": assessment_record.id,
                "workout_id": workout_record.id,
                "nutrition_id": nutrition_record.id,
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
        finally:
            db_manager.close()

# Create global instance for FastAPI or other imports (DB-enabled by default)
fitness_manager = FitnessCrewManager(local_only=False)

# For direct testing
if __name__ == "__main__":
    # TEST PROMPT
    test_input = """Hi! I'm Sarah, a 28-year-old female. I'm 5'6" tall and currently weigh 150 lbs. I'd like to get down to around 140 lbs and also build some lean muscle tone. 

I'm pretty much a beginner when it comes to structured workouts - I used to go for occasional jogs and did some yoga classes pre-pandemic, but haven't been consistent for the past 2 years. Right now I'd say I'm lightly active at best.

My main goals are weight loss and muscle toning. I'd love to see results in about 3-4 months, and my motivation is high - I have a wedding to attend and want to feel confident in my dress! 

For equipment, I have a home gym setup with dumbbells (5-25 lbs), resistance bands, a yoga mat, and access to a local gym with full equipment. I can realistically commit to working out 4 days a week, about 45-60 minutes per session. I prefer evening workouts after work.

As for diet, I'm not vegetarian but I don't eat red meat often. I have no major allergies but I'm lactose intolerant. I work a desk job so I'm sitting most of the day. I usually get about 6-7 hours of sleep and my stress level is medium due to work deadlines.

I usually skip breakfast, have a light lunch, and tend to eat my biggest meal at dinner. I'm open to changing this if it helps with my goals. Budget-wise, I'm fine with reasonable nutrition costs but nothing too expensive.

Can you help me create a workout and nutrition plan?"""
    
    print("🚀 Starting AgentJim local-only test (Gemini)...")
    local_manager = FitnessCrewManager(local_only=True)
    result = local_manager.process_user_request(test_input)
    
    if result["success"]:
        print("\n🎉 SUCCESS! (Local-only run, no DB writes)")
        print("\n— Assessment Preview —\n")
        print(result['assessment'][:1200])
        print("\n— Workout Plan Preview —\n")
        print(result['workout_plan'][:1200])
        print("\n— Nutrition Plan Preview —\n")
        print(result['nutrition_plan'][:1200])
    else:
        print(f"💥 FAILED: {result['error']}")