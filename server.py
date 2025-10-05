from fastapi import FastAPI
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from config.settings import PlanRequest, User
from crew.manager import FitnessCrewManager

app = FastAPI(name="Agent Jim Server")
manager = FitnessCrewManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/plan")
def create_plan(request: PlanRequest):
    try:
        user: User | None = request.user

        # Build a comprehensive natural language input for the crew
        name = user.name if (user and user.name) else "User"
        age = f"{user.age}-year-old" if (user and user.age is not None) else ""
        gender = user.gender.lower() if (user and user.gender) else "person"
        nationality = f"from {user.nationality}" if (user and user.nationality) else ""
        height = f"My height is {user.height} cm" if (user and user.height is not None) else ""
        weight = f"and I currently weigh {request.weight} kg." if (request.weight is not None) else ""

        goals = f"My primary goal is {request.primary_goal.lower()}."
        secondary = f" My secondary goal is {request.secondary_goal.lower()}." if request.secondary_goal else ""
        availability = (
            f" I can work out {request.workout_days} days per week for about {request.session_time} minutes per session."
            if (request.workout_days and request.session_time) else ""
        )

        additional = request.additional_details or ""

        user_input = (
            f"Hi! I'm {name}, a {age} {gender} {nationality}. {height} {weight}\n\n"
            f"{goals}{secondary}{availability}\n\n"
            f"Additional details about me:\n{additional}\n\n"
            f"Can you help me create a workout and nutrition plan that considers my background and preferences?"
        )

        print(f"🔍 User input being sent to AI: {user_input}")
        result = manager.process_user_request(user_input)

        if not result.get("success"):
            error_msg = result.get("error", "Unknown error")
            return JSONResponse(status_code=500, content={"message": error_msg})

        assessment = result.get("assessment", "")
        workout_plan = result.get("workout_plan", "")
        nutrition_plan = result.get("nutrition_plan", "")

        combined_message = (
            "ASSESSMENT\n\n" + assessment.strip() + "\n\n"
            + "WORKOUT PLAN\n\n" + workout_plan.strip() + "\n\n"
            + "NUTRITION PLAN\n\n" + nutrition_plan.strip()
        )

        return {
            "success": True,
            "message": combined_message,
            "assessment": assessment,
            "workout_plan": workout_plan,
            "nutrition_plan": nutrition_plan
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)