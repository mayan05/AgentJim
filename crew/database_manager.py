from db.database import SessionLocal
from db import crud
import re
import json

class DatabaseManager:
    def __init__(self):
        self.db = SessionLocal()
    
    def close(self):
        self.db.close()
    
    def parse_user_input(self, user_input: str):
        """Extract basic user info from input text"""
        # Simple regex patterns to extract info
        name_pattern = r"I'm ([A-Za-z]+)"
        age_pattern = r"(\d+)[-\s]*year[-s]*[-\s]*old"
        gender_pattern = r"(male|female|non-binary)"
        height_pattern = r"(\d+['\"]\d+['\"]?|\d+\.\d+\s*cm|\d+\s*cm)"
        weight_pattern = r"(\d+\s*(?:lbs?|kg|pounds?))"
        
        # Extract information
        name_match = re.search(name_pattern, user_input, re.IGNORECASE)
        age_match = re.search(age_pattern, user_input, re.IGNORECASE)
        gender_match = re.search(gender_pattern, user_input, re.IGNORECASE)
        height_match = re.search(height_pattern, user_input, re.IGNORECASE)
        weight_match = re.search(weight_pattern, user_input, re.IGNORECASE)
        
        return {
            "name": name_match.group(1) if name_match else "User",
            "age": int(age_match.group(1)) if age_match else None,
            "gender": gender_match.group(1).title() if gender_match else "Not specified",
            "height": height_match.group(1) if height_match else "Not specified",
            "weight": weight_match.group(1) if weight_match else "Not specified"
        }
    
    def create_user_session(self, user_input: str):
        """Create user and return user_id"""
        user_info = self.parse_user_input(user_input)
        
        user = crud.create_user(
            db=self.db,
            name=user_info["name"],
            age=user_info["age"] or 0,
            gender=user_info["gender"],
            height=user_info["height"],
            weight=user_info["weight"]
        )
        return user.id
    
    def save_assessment(self, user_id: int, assessment_output: str):
        """Save assessment result"""
        return crud.save_assessment(self.db, user_id, assessment_output)
    
    def save_workout_plan(self, user_id: int, workout_output: str):
        """Save workout plan result"""
        return crud.save_workout_plan(self.db, user_id, workout_output)
    
    def save_nutrition_plan(self, user_id: int, nutrition_output: str):
        """Save nutrition plan result"""
        return crud.save_nutrition_plan(self.db, user_id, nutrition_output)