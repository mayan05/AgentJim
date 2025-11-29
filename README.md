# AgentJim 💪

AgentJim is a multi-agentic AI fitness trainer designed to create hyper-personalized workout and nutrition plans. It leverages a team of AI agents working in harmony to assess your profile, design a workout split, and craft a nutrition strategy tailored to your specific goals and lifestyle.

## 🚀 Features

-   **Personalized Assessment**: Analyzes your age, gender, goals, experience level, and equipment availability.
-   **Custom Workout Plans**: Generates detailed weekly workout splits (sets, reps, rest) based on your profile.
-   **Nutrition Strategy**: Provides calorie targets, macro splits, and meal options aligned with your fitness goals.
-   **Multi-Agent Architecture**: Uses specialized agents for assessment, workout planning, and nutrition.

## 🛠️ Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/)
-   **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
-   **AI Orchestration**: [CrewAI](https://crewai.com/)
-   **LLM Interface**: [LangChain](https://www.langchain.com/)
-   **Models**: Supports Groq (Llama 3) and Google Gemini.

## 🏗️ Architecture

The application follows a client-server architecture:

1.  **Streamlit App**: Collects user inputs and displays the final plan.
2.  **FastAPI Server**: Receives the request and triggers the AI crew.
3.  **CrewAI Manager**: Orchestrates three sequential agents:
    -   **Assessment Agent**: Extracts and profiles user data.
    -   **Workout Planner**: Creates the training program based on the assessment.
    -   **Nutrition Agent**: Develops a diet plan complementing the workout.

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd AgentJim
    ```

2.  **Install dependencies**:
    This project uses `uv` for dependency management.
    ```bash
    uv sync
    # OR using pip
    pip install -e .
    ```

3.  **Environment Setup**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    GROQ_API_KEY=your_groq_api_key
    GEMINI_API_KEY=your_gemini_api_key
    FASTAPI_URL=http://localhost:8000
    ```

## 🏃‍♂️ Usage

1.  **Start the Backend Server**:
    ```bash
    python server.py
    ```
    The server will start on `http://localhost:8000`.

2.  **Run the Frontend App**:
    ```bash
    streamlit run app.py
    ```

3.  Open your browser to the Streamlit URL (usually `http://localhost:8501`) and start your fitness journey!

---
Built with ❤️ using CrewAI, LangChain, and Streamlit.
