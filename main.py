import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# 1. Cargar variables de entorno (.env)
load_dotenv()

# 2. Configurar el modelo (Usando la clase LLM de CrewAI)
# Nota: Si gemini-1.5-flash sigue dando error de cuota (429), 
# podrías cambiar el string a "groq/llama-3.3-70b-versatile" más tarde.
gemini_llm = LLM(
    model="google/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

# 3. Definir el Agente
researcher = Agent(
    role='Tech Visionary',
    goal='Analyze the potential of Agentic AI in 2026',
    backstory="""You are a specialized AI agent in the AgentFactory. 
    Your mission is to explore how autonomous agents are changing 
    software development on portable devices like the Surface Book.""",
    allow_delegation=False,
    verbose=True,
    llm=gemini_llm
)

# 4. Definir la Tarea
task1 = Task(
    description="""Write a 3-bullet point summary about why 
    developing Agentic AI in 2026 is a game changer.""",
    expected_output="A concise 3-bullet point summary in English.",
    agent=researcher
)

# 5. Instanciar la Crew (El equipo)
factory_crew = Crew(
    agents=[researcher],
    tasks=[task1],
    process=Process.sequential
)

# 6. ¡Arrancar el proceso!
print("### Starting AgentFactory v1.0 ###")
try:
    result = factory_crew.kickoff()
    print("\n\n########################")
    print("## AGENT OUTPUT:")
    print(result)
    print("########################")
except Exception as e:
    print(f"\n❌ Oops! Algo salió mal: {e}")