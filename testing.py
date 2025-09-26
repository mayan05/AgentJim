import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from crewai import Agent, Task, Crew, Process

# Load environment variables
load_dotenv()

def test_groq_direct():
    print("🧪 Testing Groq model directly...")
    
    # Check if API key exists
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found in environment")
        return False
    
    print(f"✅ Found Groq API key: {api_key[:10]}...")
    
    try:
        # Initialize Groq model
        groq_llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=api_key,
            temperature=0.7,
            max_tokens=1000,
            max_retries=2
        )
        
        # Simple test message
        test_prompt = "Hello! Please respond with a short fitness tip in 2-3 sentences."
        
        print("🔄 Sending test message to Groq...")
        response = groq_llm.invoke(test_prompt)
        
        print("✅ Groq responded successfully!")
        print(f"Response: {response.content}")
        return True
        
    except Exception as e:
        print(f"❌ Groq test failed: {str(e)}")
        return False

def test_crewai_with_groq():
    """Test CrewAI (simplified version)"""
    print("\n🤖 Testing CrewAI...")
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("❌ API_KEY not found")
        return False
    
    try:
        # Initialize Groq model for CrewAI
        groq_llm = ChatGroq(
            model="groq/llama-3.3-70b-versatile",
            api_key=api_key,
            temperature=0.7,
            max_tokens=1500,
            max_retries=2
        )
        
        # Create a simple fitness assessment agent
        assessment_agent = Agent(
            role="Fitness Assessment Specialist",
            goal="Analyze user input and provide a basic fitness assessment",
            backstory="You are an experienced fitness consultant who helps people understand their current fitness situation and goals.",
            llm=groq_llm,
            verbose=True
        )
        
        # Create a simple task
        assessment_task = Task(
            description="Analyze the user's fitness information and provide a basic assessment with key insights and recommendations.",
            agent=assessment_agent,
            expected_output="""
            BASIC FITNESS ASSESSMENT:
            - Current Situation: [Brief summary]
            - Key Goals: [Main objectives]
            - Recommendations: [2-3 main suggestions]
            - Next Steps: [What to focus on first]
            """
        )
        
        # Create a simple crew with one agent
        crew = Crew(
            agents=[assessment_agent],
            tasks=[assessment_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Test input
        test_input = """Hi! I'm Sarah, 28 years old, 5'6" and 150 lbs. I want to lose 10 lbs and get more toned. 
        I'm a beginner and can work out 3-4 times per week. I have basic home gym equipment."""
        
        print("🔄 Running CrewAI...")
        result = crew.kickoff({"input": test_input})
        
        print("✅ CrewAI with Groq completed successfully!")
        print(f"Result: {str(result)}")
        return True
        
    except Exception as e:
        print(f"❌ CrewAI with Groq failed: {str(e)}")
        return False

def main():
    print("🚀 Starting Local Test ")
    print("=" * 50)
    
    direct_success = test_groq_direct()
    
    if direct_success:
        print("\n" + "=" * 50)
        crew_success = test_crewai_with_groq()
        
        if crew_success:
            print(f"\n🎉Testing is correctly.")
        else:
            print(f"\n⚠️ Direct API works but CrewAI integration has issues.")
    else:
        print(f"\n💥 Test failed. Check your API key and internet connection.")

if __name__ == "__main__":
    main()
