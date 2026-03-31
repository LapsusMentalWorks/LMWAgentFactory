import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

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
    
# 3. Definir las Herramientas
@tool("actualizar_fichero_progreso")
def actualizar_fichero_progreso(contenido: str) -> str:
    """Útil para guardar el estado del proyecto en PROGRESS.md. 
    Debe usarse al final de cada sesión para persistir los aprendizajes y el nuevo backlog."""
    try:
        with open("PROGRESS.md", "w", encoding="utf-8") as f:
            f.write(contenido)
        return "PROGRESS.md actualizado correctamente."
    except Exception as e:
        return f"Error al actualizar el archivo: {e}"



# 4. Definir los Agentes
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
    goal='Explicar conceptos técnicos y asegurar que PROGRESS.md esté actualizado.',
    backstory="""Eres el guardián del conocimiento de AgentsFactory. 
    Tu misión es doble: 
    1. Explicar el 'porqué' de lo que se ha implementado (método Feynman).
    2. Usar tu herramienta de escritura para reflejar los cambios en PROGRESS.md, 
       marcando iteraciones como completadas y pegando el nuevo backlog del PM.
       Hazlo siguiendo el ejemplo de iteraciones anteriores para mantener la coherencia del historial.""", # <--- ENFOQUE EN DOCUMENTACIÓN Y EXPLICACIÓN
    tools=[actualizar_fichero_progreso], # <--- Capacidad añadida
    llm=gemini_llm,
    verbose=True
)

# 5. Definir las Tareas
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
        description="""1. Analiza el backlog de la Iteración 3 propuesto por el PM.
        2. Redacta el 'Debriefing de la Sesión' explicando el 'porqué' de cada tarea propuesta (método Feynman).
        3. Genera el contenido completo para el nuevo PROGRESS.md de manera muy resumida, siguiendo el formato de iteraciones anteriores.:
        - Cambia el estado de la Iteración 2 a '✅ Completada'.
        - Añade el backlog de la Iteración 3 en la sección correspondiente.
        4. USA la herramienta 'actualizar_fichero_progreso' para guardar los cambios en el disco.""",
        expected_output="Confirmación de que el archivo ha sido actualizado y un breve resumen de la teoría.",
        agent=tutor_ia,
        context=[tarea_pm]
    )
    return [tarea_pm, tarea_tutor]

# 6. ¡Arrancar el proceso!
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