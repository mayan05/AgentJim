from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from config.settings import PlanRequest

app = FastAPI(name="Agent Jim Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/plan")
def create_plan(request: PlanRequest):
    return {"message": "FastAPI server works!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)