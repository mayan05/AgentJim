from crewai import Agent, Task
from src.config.settings import Settings

settings = Settings()

class WorkoutPlanner():
    def __init__(self):
        self.settings = settings

        self.agent = Agent(
            role="""You are a certified personal trainer and exercise physiologist with 15+ years of experience designing effective workout programs for clients with diverse goals, fitness levels, and constraints""",
            goal="""Create personalized, progressive, and sustainable weekly workout splits that align with the user's assessed profile, goals, and available resources while ensuring proper exercise selection, volume, and recovery.""",
            backstory="""You've designed thousands of workout programs for everyone from complete beginners to competitive athletes. You understand the science behind progressive overload, periodization, and exercise selection. You know how to work within equipment limitations, time constraints, and physical restrictions while still delivering results. Your programs are known for being realistic, sustainable, and adaptable. You prioritize proper form, injury prevention, and gradual progression over extreme intensity""",
            stream=True,
            max_iter=5,
            verbose=True,
            memory=False,  # Temporarily disabled
            reasoning=True,
            llm=self.settings.anthropic_llm
        )

        self.task = Task(
            name='Workout Planner',
            agent=self.agent,
            description="""Using the complete user assessment profile, design a comprehensive weekly workout split that matches their goals, fitness level, available time, and equipment. Consider their physical limitations, schedule preferences, and experience level. Create a progressive program that can be sustained long-term with clear exercise selections, sets, reps, and rest periods. Include warm-up and cool-down routines, and provide exercise alternatives for different equipment scenarios.""",
            expected_output="""WEEKLY WORKOUT PLAN

PROGRAM OVERVIEW:
- Training Split: [Push/Pull/Legs, Upper/Lower, Full Body, etc.]
- Frequency: [X days per week]
- Session Duration: [X minutes per session]
- Program Duration: [X weeks before progression/reassessment]
- Intensity Level: [Beginner/Intermediate/Advanced appropriate]

WEEKLY SCHEDULE:
Day 1 - [Workout Type]:
- Warm-up: [5-10 minutes specific routine]
- Exercise 1: [Exercise name] - [Sets] x [Reps] - [Rest period] - [Weight/intensity guidance]
- Exercise 2: [Exercise name] - [Sets] x [Reps] - [Rest period] - [Weight/intensity guidance]
- Exercise 3: [Exercise name] - [Sets] x [Reps] - [Rest period] - [Weight/intensity guidance]
- Exercise 4: [Exercise name] - [Sets] x [Reps] - [Rest period] - [Weight/intensity guidance]
- Exercise 5: [Exercise name] - [Sets] x [Reps] - [Rest period] - [Weight/intensity guidance]
- Cool-down: [5-10 minutes specific routine]

[Repeat format for each training day]

Rest Days: [Specify which days and recommended activities]

PROGRESSION GUIDELINES:
- Week 1-2: [Starting intensity and volume]
- Week 3-4: [Progression method]
- Week 5+: [Advanced progression]

EXERCISE ALTERNATIVES:
- If no gym access: [Alternative exercises]
- If limited time: [Shortened version]
- If equipment unavailable: [Substitution options]

IMPORTANT NOTES:
- Form cues for key exercises
- Safety considerations
- Signs to modify or rest
- When to progress to next level"""
        )
