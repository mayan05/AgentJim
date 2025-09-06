from db.database import create_tables, SessionLocal
import db.crud as crud

# Create tables
create_tables()

# Test database
db = SessionLocal()

# Create a test user
user = crud.create_user(
    db=db, 
    name="Test User", 
    age=25, 
    gender="Male", 
    height="5'10\"", 
    weight="70kg"
)

print(f"Created user with ID: {user.id}")

# Save test assessment
assessment = crud.save_assessment(
    db=db,
    user_id=user.id,
    assessment_data="Test assessment data"
)

print(f"Saved assessment with ID: {assessment.id}")

db.close()
print("Database test completed!")