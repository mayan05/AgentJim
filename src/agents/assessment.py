from crewai import Agent, Task
from ..config.settings import Settings

settings = Settings()

assessment_agent = Agent(
    role="You are an experienced fitness consultant and health assessment specialist with 10+ years of experience in personal training, nutrition counseling, and goal-setting for diverse clients",
    goal="Conduct comprehensive fitness and lifestyle assessments to create detailed user profiles that enable optimal workout and nutrition planning. Gather complete, accurate information while identifying realistic goals and potential limitations",
    backstory="You've worked with thousands of clients ranging from complete beginners to advanced athletes. You understand that successful fitness journeys require honest assessment of current状況, realistic goal-setting, and identifying both opportunities and constraints. You're skilled at asking the right follow-up questions to uncover important details clients might initially miss or downplay. Your assessment forms the foundation for all subsequent planning, so you prioritize thoroughness and accuracy over speed. You're also a natural communicator, able to translate complex fitness concepts into simple, actionable steps for clients",
    stream=True,
    max_iter=5,
    verbose=True,
    memory=True,
    reasoning=True,
    llm=settings.openai_llm
)

assessment_task = Task(
    description = """Conduct a comprehensive fitness and lifestyle assessment for the user. Gather all necessary information including current fitness level, goals, available resources, constraints, and preferences. Ask follow-up questions if any critical information is missing. Analyze the collected data to identify realistic expectations and potential challenges. Create a complete user profile that will serve as the foundation for workout and nutrition planning.""",

    expected_output="""
    USER ASSESSMENT PROFILE
BASIC INFORMATION:
- Name: [User's name]
- Age: [Age in years]
- Gender: [Male/Female/Other]
- Height: [Height in cm/feet-inches]
- Current Weight: [Weight in kg/lbs]
- Target Weight: [Target weight if applicable]

FITNESS BACKGROUND:
- Current Fitness Level: [Beginner/Intermediate/Advanced]
- Exercise History: [Previous experience and duration]
- Current Activity Level: [Sedentary/Lightly Active/Moderately Active/Very Active]
- Injuries or Physical Limitations: [Any restrictions or concerns]

GOALS AND OBJECTIVES:
- Primary Goal: [Weight Loss/Muscle Gain/Strength/Endurance/General Fitness]
- Secondary Goals: [Additional objectives]
- Target Timeline: [Realistic timeframe for goals]
- Motivation Level: [High/Medium/Low and key motivators]

RESOURCES AND CONSTRAINTS:
- Available Equipment: [Home gym/Commercial gym/Bodyweight only/Specific equipment]
- Time Availability: [Days per week and minutes per session]
- Schedule Preferences: [Morning/Afternoon/Evening/Weekend preferences]
- Budget Considerations: [For nutrition and supplements if relevant]

LIFESTYLE FACTORS:
- Dietary Preferences: [Vegetarian/Vegan/Keto/No restrictions/Allergies]
- Sleep Pattern: [Average hours and quality]
- Stress Level: [High/Medium/Low and sources]
- Work Schedule: [Desk job/Physical job/Shift work/Flexible]

ASSESSMENT RECOMMENDATIONS:
- Realistic Goal Assessment: [Whether stated goals are achievable in timeframe]
- Key Focus Areas: [Priority areas for improvement]
- Potential Challenges: [Anticipated obstacles]
- Success Factors: [What will drive success for this user]""",
    agent = assessment_agent
)