from sqlalchemy.orm import Session
from .models import User, Assessment, WorkoutPlan, NutritionPlan
import json

def create_user(db: Session, name: str, age: int, gender: str, height: str, weight: str):
    user = User(
        name=name,
        age=age,
        gender=gender,
        height=height,
        current_weight=weight
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def save_assessment(db: Session, user_id: int, assessment_data: str):
    assessment = Assessment(
        user_id=user_id,
        assessment_data=assessment_data
    )
    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    return assessment

def save_workout_plan(db: Session, user_id: int, plan_data: str):
    workout = WorkoutPlan(
        user_id=user_id,
        plan_data=plan_data
    )
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

def save_nutrition_plan(db: Session, user_id: int, plan_data: str):
    nutrition = NutritionPlan(
        user_id=user_id,
        plan_data=plan_data
    )
    db.add(nutrition)
    db.commit()
    db.refresh(nutrition)
    return nutrition

def get_user_plans(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return {
            "user": user,
            "assessments": user.assessments,
            "workout_plans": user.workout_plans,
            "nutrition_plans": user.nutrition_plans
        }
    return None