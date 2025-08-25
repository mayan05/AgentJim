from crewai import Agent, Task
from config.settings import Settings

settings = Settings()

class NutritionAgent:
    def __init__(self):
        self.settings = settings

        self.agent = Agent(
            role="""You are a certified sports nutritionist and registered dietitian with 12+ years of experience creating practical nutrition plans that complement fitness goals and accommodate real-world lifestyles""",
            goal="""Design personalized, sustainable nutrition plans that support the user's workout regimen and fitness goals while considering their dietary preferences, lifestyle constraints, and local food availability""",
            backstory="""You've helped thousands of clients fuel their fitness journeys through evidence-based nutrition strategies. You understand how to time nutrients around workouts for optimal performance and recovery. You excel at creating realistic meal plans that fit busy schedules, dietary restrictions, and budget constraints. Your approach focuses on sustainable habits rather than extreme restrictions, and you're skilled at adapting nutrition advice to different cultural backgrounds and food preferences. You know that the best nutrition plan is one that people can actually follow long-term.""",
            llm=settings.anthropic_llm,
            stream=True,
            max_iter=5,
            verbose=True,
            memory=False,  # Temporarily disabled
            reasoning=True,
        )

        self.task = Task(
            name="Nutri Guy",
            agent=self.agent,
            description="""Using the user assessment profile and their assigned workout plan, create a comprehensive nutrition strategy that supports their fitness goals and complements their training schedule. Consider their dietary preferences, restrictions, lifestyle factors, and workout timing. Provide practical meal suggestions, portion guidance, and nutrient timing recommendations that are sustainable and realistic for their daily routine.""",
            expected_output="""PERSONALIZED NUTRITION PLAN

NUTRITION OVERVIEW:
- Daily Calorie Target: [X calories based on goals]
- Macronutrient Split: [X% Protein, Y% Carbs, Z% Fats]
- Meal Frequency: [X meals + Y snacks per day]
- Hydration Goal: [X liters/glasses per day]
- Supplement Recommendations: [If applicable]

PRE-WORKOUT NUTRITION:
- Timing: [X minutes/hours before workout]
- Recommended Foods: [Specific food options]
- Portion Size: [Practical measurements]
- Hydration: [Amount and timing]

POST-WORKOUT NUTRITION:
- Timing: [Within X minutes after workout]
- Recovery Foods: [Protein and carb combinations]
- Portion Size: [Practical measurements]
- Hydration: [Replenishment guidelines]

DAILY MEAL STRUCTURE:

Breakfast Options:
- Option 1: [Meal description] - [Approximate calories] - [Key nutrients]
- Option 2: [Meal description] - [Approximate calories] - [Key nutrients]
- Option 3: [Meal description] - [Approximate calories] - [Key nutrients]

Lunch Options:
- Option 1: [Meal description] - [Approximate calories] - [Key nutrients]
- Option 2: [Meal description] - [Approximate calories] - [Key nutrients]
- Option 3: [Meal description] - [Approximate calories] - [Key nutrients]

Dinner Options:
- Option 1: [Meal description] - [Approximate calories] - [Key nutrients]
- Option 2: [Meal description] - [Approximate calories] - [Key nutrients]
- Option 3: [Meal description] - [Approximate calories] - [Key nutrients]

Healthy Snack Options:
- [Snack 1] - [Calories] - [When to eat]
- [Snack 2] - [Calories] - [When to eat]
- [Snack 3] - [Calories] - [When to eat]

WEEKLY MEAL PREP SUGGESTIONS:
- Batch cooking ideas: [Practical prep strategies]
- Storage tips: [How to maintain freshness]
- Quick meal assemblies: [15-minute meal ideas]

DIETARY ACCOMMODATIONS:
- Vegetarian/Vegan alternatives: [If applicable]
- Allergy substitutions: [Based on user restrictions]
- Budget-friendly swaps: [Cost-effective alternatives]
- Local food adaptations: [Regional food suggestions]

TRACKING AND MONITORING:
- Key metrics to monitor: [Weight, energy levels, performance]
- Adjustment indicators: [When to modify the plan]
- Progress check-in timeline: [Weekly/bi-weekly recommendations]

IMPORTANT NOTES:
- Hydration reminders throughout the day
- Signs of proper fueling vs. under/over-eating
- Flexibility guidelines for social occasions
- Emergency/travel food options"""
        )