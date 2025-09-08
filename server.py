from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crew.manager import FitnessCrewManager
import uvicorn

app = FastAPI(title="AgentJim - AI Fitness Trainer")

# Initialize crew manager
crew_manager = FitnessCrewManager()

class UserRequest(BaseModel):
    message: str

class FitnessResponse(BaseModel):
    success: bool
    user_id: int = None
    assessment: str = None
    workout_plan: str = None
    nutrition_plan: str = None
    error: str = None

@app.get("/")
async def root():
    return {"message": "Welcome to AgentJim - Your AI Fitness Trainer!"}

@app.post("/create-fitness-plan", response_model=FitnessResponse)
async def create_fitness_plan(request: UserRequest):
    """Create personalized fitness and nutrition plan"""
    try:
        result = crew_manager.process_user_request(request.message)
        
        if result["success"]:
            return FitnessResponse(
                success=True,
                user_id=result["user_id"],
                assessment=result["assessment"],
                workout_plan=result["workout_plan"],
                nutrition_plan=result["nutrition_plan"]
            )
        else:
            raise HTTPException(status_code=500, detail=result["error"])
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)