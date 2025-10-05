import streamlit as st
from crew.manager import FitnessCrewManager
import json
import requests
import os
from config.settings import User, PlanRequest

server_url = os.environ.get("FASTAPI_URL")

# Page config
st.set_page_config(
    page_title="AgentJim", 
    page_icon="💪",
    layout="wide"
)

# Title and description
st.title("💪 AgentJim - Your AI Fitness Trainer")
st.markdown("Get personalized workout and nutrition plans created by AI agents!")

# Sidebar for user info
with st.sidebar:
    st.header("📝 Tell us about yourself")
    
    # Basic info
    name = st.text_input("Name", placeholder="e.g., Sarah")
    age = st.number_input("Age", min_value=16, max_value=80, value=20)
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
    nationality = st.text_input("Nationality/Country", placeholder="e.g., Indian, American, British")
    
    # Physical measurements
    st.subheader("📏 Physical Details")
    height = st.number_input("Height (cm)", min_value=120, max_value=250, value=170, step=1)
    weight = st.number_input("Current Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)
    
    st.subheader("🎯 Your Goals")
    primary_goal = st.selectbox("Primary Goal", [
        "Weight Loss", "Muscle Gain", "General Fitness", 
        "Strength Training", "Endurance", "Toning"
    ])
    
    secondary_goal = st.selectbox("Secondary Goal (Optional)", [
        "None", "Weight Loss", "Muscle Gain", "General Fitness", 
        "Strength Training", "Endurance", "Toning", "Flexibility", 
        "Better Sleep", "Stress Relief", "Increased Energy"
    ])
    
    st.subheader("⏰ Availability")
    workout_days = st.slider("Days per week", min_value=1, max_value=7, value=4)
    session_time = st.slider("Minutes per session", min_value=15, max_value=120, value=45, step=5)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💬 Additional Details")
    user_details = st.text_area(
        "Tell us more about your fitness background, equipment available, dietary preferences, etc.",
        height=200,
        placeholder="""Example: I'm a beginner with home gym equipment (dumbbells, resistance bands). I work a desk job and prefer evening workouts. I'm lactose intolerant and usually skip breakfast. I have no major injuries but sometimes get lower back pain from sitting too much..."""
    )

with col2:
    st.subheader("🚀 Generate Your Plan")
    
    # Display user summary
    with st.expander("👀 Preview Your Info"):
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age} years old")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Nationality:** {nationality}")
        st.write(f"**Height:** {height} cm")
        st.write(f"**Weight:** {weight} kg")
        st.write(f"**Primary Goal:** {primary_goal}")
        if secondary_goal != "None":
            st.write(f"**Secondary Goal:** {secondary_goal}")
        st.write(f"**Availability:** {workout_days} days/week, {session_time} min/session")
    
    if st.button("Create My Fitness Plan", type="primary", use_container_width=True):
        if nationality and user_details and name:
            user_deets = PlanRequest(
                user=User(
                    name=name,
                    age=age,
                    gender=gender,
                    nationality=nationality,
                    height=height
                ),
                weight=weight,
                primary_goal=primary_goal,
                secondary_goal=secondary_goal,
                workout_days=workout_days,
                session_time=session_time,
                additional_details=user_details
            )

            # Show loading
            with st.spinner("Agents are working on your plan. Please wait..."):
                try:
                    response = requests.post(url=f"{server_url}/plan", json=user_deets.model_dump(), timeout=60)
                    plan = response.json()
                    if response.status_code == 200:
                        # Store the plan in session state to display it below
                        st.session_state['fitness_plan'] = plan
                        st.success("🎉 Your plan is ready!")
                        st.rerun()
                    else:
                        st.error(f"Error: {plan['message']}")
                except Exception as e:
                    st.error(f"Error: {e}")
        
        else:
            st.warning("Have you filled in your name, nationality, and additional details?!")

# Display the plan below the columns, centered
if 'fitness_plan' in st.session_state:
    st.markdown("---")
    st.markdown("## 📋 Your Personalized Fitness Plan")
    st.markdown("---")
    
    # Display the plan in a centered container with styling
    st.markdown("""
    <div style="
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
        margin: 20px 0;
    ">
    """, unsafe_allow_html=True)
    
    st.markdown(st.session_state['fitness_plan']["message"])
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("Built with ❤️ using Streamlit, LangChain and CrewAI")