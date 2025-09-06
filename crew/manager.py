from crewai import Crew, Process
from crew.agents import assessment, nutriagent, workout_planner

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
    memory=False  # Disabled due to path length issue
)



    
# TEST PROMPT
"""Hi! I'm Sarah, a 28-year-old female. I'm 5'6" tall and currently weigh 150 lbs. I'd like to get down to around 140 lbs and also build some lean muscle tone. 

I'm pretty much a beginner when it comes to structured workouts - I used to go for occasional jogs and did some yoga classes pre-pandemic, but haven't been consistent for the past 2 years. Right now I'd say I'm lightly active at best.

My main goals are weight loss and muscle toning. I'd love to see results in about 3-4 months, and my motivation is high - I have a wedding to attend and want to feel confident in my dress! 

For equipment, I have a home gym setup with dumbbells (5-25 lbs), resistance bands, a yoga mat, and access to a local gym with full equipment. I can realistically commit to working out 4 days a week, about 45-60 minutes per session. I prefer evening workouts after work.

As for diet, I'm not vegetarian but I don't eat red meat often. I have no major allergies but I'm lactose intolerant. I work a desk job so I'm sitting most of the day. I usually get about 6-7 hours of sleep and my stress level is medium due to work deadlines.

I usually skip breakfast, have a light lunch, and tend to eat my biggest meal at dinner. I'm open to changing this if it helps with my goals. Budget-wise, I'm fine with reasonable nutrition costs but nothing too expensive.

Can you help me create a workout and nutrition plan?"""
# shall use this for testing later on