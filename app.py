import streamlit as st
from crew.manager import fitness_manager
import time

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
    age = st.number_input("Age", min_value=16, max_value=80, value=25)
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
    workout_days = st.slider("Days per week", 1, 7, 4)
    session_time = st.slider("Minutes per session", 15, 120, 45)

# Main content area
col1, col2 = st.columns([2, 1])

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
        if name and nationality and user_details:
            # Build complete user input
            secondary_goal_text = f" My secondary goal is {secondary_goal.lower()}." if secondary_goal != "None" else ""
            
            complete_input = f"""Hi! I'm {name}, a {age}-year-old {gender.lower()} from {nationality}. My height is {height} cm and I currently weigh {weight} kg. 
            
My primary goal is {primary_goal.lower()}.{secondary_goal_text} I can work out {workout_days} days per week for about {session_time} minutes per session.

Additional details about me:
{user_details}

Can you help me create a workout and nutrition plan that considers my cultural background and local food availability?"""

            # Show loading
            with st.spinner("🤖 AI agents are working on your personalized plan..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulate progress updates
                status_text.text("🔍 Assessment agent analyzing your profile...")
                progress_bar.progress(25)
                time.sleep(1)
                
                status_text.text("💪 Workout planner designing your routine...")
                progress_bar.progress(50)
                
                result = fitness_manager.process_user_request(complete_input)
                
                status_text.text("🥗 Nutrition agent creating your meal plan...")
                progress_bar.progress(75)
                time.sleep(0.5)
                
                status_text.text("✨ Finalizing your personalized plan...")
                progress_bar.progress(100)
                time.sleep(0.5)
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            if result["success"]:
                st.success("✅ Your personalized plan is ready!")
                
                # Store results in session state
                st.session_state.assessment = result["assessment"]
                st.session_state.workout_plan = result["workout_plan"]
                st.session_state.nutrition_plan = result["nutrition_plan"]
                st.session_state.plan_generated = True
                st.session_state.user_name = name
                
            else:
                st.error(f"❌ Error: {result['error']}")
        else:
            st.warning("Please fill in your name, nationality, and additional details!")

# Display results if available
if hasattr(st.session_state, 'plan_generated') and st.session_state.plan_generated:
    st.divider()
    st.header(f"📋 Your Personalized Fitness Plan, {st.session_state.user_name}!")
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["📊 Assessment", "💪 Workout Plan", "🥗 Nutrition Plan"])
    
    with tab1:
        st.subheader("User Assessment Profile")
        st.text_area("Assessment Details", st.session_state.assessment, height=400, disabled=True)
        
        # Download button
        st.download_button(
            label="📥 Download Assessment",
            data=st.session_state.assessment,
            file_name=f"{st.session_state.user_name}_assessment.txt",
            mime="text/plain"
        )
        
    with tab2:
        st.subheader("Weekly Workout Plan")
        st.text_area("Workout Details", st.session_state.workout_plan, height=400, disabled=True)
        
        # Download button
        st.download_button(
            label="📥 Download Workout Plan",
            data=st.session_state.workout_plan,
            file_name=f"{st.session_state.user_name}_workout_plan.txt",
            mime="text/plain"
        )
        
    with tab3:
        st.subheader("Personalized Nutrition Plan")
        st.text_area("Nutrition Details", st.session_state.nutrition_plan, height=400, disabled=True)
        
        # Download button
        st.download_button(
            label="📥 Download Nutrition Plan",
            data=st.session_state.nutrition_plan,
            file_name=f"{st.session_state.user_name}_nutrition_plan.txt",
            mime="text/plain"
        )
    
    # Reset button
    st.divider()
    if st.button("🔄 Create New Plan", type="secondary"):
        # Clear session state
        for key in ['assessment', 'workout_plan', 'nutrition_plan', 'plan_generated', 'user_name']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Footer
st.divider()
st.markdown("Built with ❤️ using Streamlit, LangChain and CrewAI")