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

class AgentsFactorySession:
    def __init__(self, iteracion_n):
        self.iteracion_n = iteracion_n
        self.archivo_progreso = "PROGRESS.md"
        self.contenido_progreso = "" # Variable para guardar el texto

    def iniciar_sesion(self):
        print(f"--- Iniciando Iteración {self.iteracion_n} ---")
        try:
            with open(self.archivo_progreso, "r", encoding="utf-8") as f:
                self.contenido_progreso = f.read()
            print("✅ Historial de progreso cargado con éxito.")
        except FileNotFoundError:
            self.contenido_progreso = "No hay historial previo. Este es el inicio del proyecto."
            print("⚠️ No se encontró PROGRESS.md, iniciando desde cero.")

    def finalizar_sesion(self, resultado_final):
        print(f"--- Finalizando Iteración {self.iteracion_n} ---")
        # Lógica para persistir el cambio en el MD (o dejar que el Tutor lo haga)
        print("Sesión documentada y guardada.")

# 3. Definir los Agentes
project_manager = Agent(
    role='Project Manager de AgentsFactory',
    goal='Diseñar iteraciones de aprendizaje de máximo 3 días para un desarrollador solitario.', # <--- LIMITACIÓN TEMPORAL
    backstory="""Eres un experto en metodología Lean y aprendizaje incremental. 
    Tu misión es dividir el progreso en pasos pequeños, tangibles y ejecutables 
    en una Surface 2 (16GB RAM). 
    
    REGLAS CRÍTICAS:
    1. Una iteración NO es un producto completo; es un experimento técnico.
    2. Evita sugerir arquitecturas pesadas (APIs, Bases de Datos, Frontends) 
       a menos que el usuario lo pida explícitamente.
    3. Céntrate en la lógica de CrewAI y la interacción entre agentes.
    4. Cada iteración debe poder completarse escribiendo un solo script de Python.""", # <--- FOCO EN SIMPLICIDAD
    llm=gemini_llm,
    verbose=True
)

tutor_ia = Agent(
    role='Tutor de Aprendizaje Agentic AI',
    goal='Explicar los conceptos técnicos y generar un resumen de aprendizaje al final.',
    backstory="""Eres un mentor pedagógico. No solo resumes lo que se hizo, sino que 
    explicas el 'porqué' técnico (arquitectura, patrones) y dejas retos para profundizar.""",
    llm=gemini_llm,
    verbose=True
)

# 4. Definir las Tareas
def crear_tareas(session, project_manager, tutor_ia):
    tarea_pm = Task(
        description=f"""Analiza los requisitos del proyecto basándote en el historial:
        
            --- INICIO DEL HISTORIAL ---
            {session.contenido_progreso}
            --- FIN DEL HISTORIAL ---
        
            Define los pasos técnicos simplificados para la Iteración 3.""",
        expected_output="Un backlog detallado de tareas técnicas para la siguiente fase.",
        agent=project_manager
    )

    tarea_tutor = Task(
        description=f"""Revisa lo propuesto por el PM y redacta el 'Debriefing de la Sesión'. 
        Incluye una sección de 'Teoría Aplicada' y actualiza el estado en el archivo PROGRESS.md.""",
        expected_output="Un bloque de texto en formato Markdown listo para el archivo de progreso.",
        agent=tutor_ia,
        context=[tarea_pm] # El tutor necesita saber qué hizo el PM
    )
    return [tarea_pm, tarea_tutor]

# 5. ¡Arrancar el proceso!
if __name__ == "__main__":
    print("### Starting AgentFactory v1.0 ###")
    try:
        # Iniciamos la sesión primero para cargar el archivo
        session = AgentsFactorySession(iteracion_n=2)
        session.iniciar_sesion()
        
        # Ahora que 'session' tiene el contenido, creamos las tareas
        tareas = crear_tareas(session, project_manager, tutor_ia)
        
        # Instanciar la Crew con las tareas creadas
        factory_crew = Crew(
            agents=[project_manager, tutor_ia],
            tasks=tareas,
            process=Process.sequential
        )
        
        resultado = factory_crew.kickoff()
        session.finalizar_sesion(resultado)
        
    except Exception as e:
        print(f"\n❌ Oops! Algo salió mal: {e}")