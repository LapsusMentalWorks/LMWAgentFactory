# 🏭 AgentsFactory - Registro de Progreso y Roadmap

## 📋 Información General
- **Objetivo:** Aprendizaje incremental de Agentic AI (Tecnologías 2026).
- **Metodología:** Ciclos de **Iteración** (3-4 días de duración).
- **Hardware Base:** Microsoft Surface 2 (16 GB RAM + GPU dedicada).
- **Stack Tecnológico:** Python 3.12, CrewAI, Gemini 2.5 Flash/Pro, Ollama (Modelos 8B-11B).

---

## 🚦 Estado Actual
- **Fase:** Iteración 2: El Mando Central (En curso) 🏗️

---

## 📅 Historial de Iteraciones

### Iteración 1: Cimientos y Orquestación ✅
- **Estado:** Completada.
- **Descripción:** Configuración inicial, creación de un agente y una tarea básica para familiarización con el framework.
- **Hitos:**
  - Configuración del entorno virtual (`venv`) y Python 3.12.
  - Integración exitosa de CrewAI con Gemini 2.5 Flash.
  - Validación de la comunicación base entre agentes y LLM.
- **Aprendizajes Clave:** 
  - Instalación de CrewAI.
  - Definición de `Agent` y `Task`.
  - Ejecución de un `Crew` simple.
  - Configuración de LLM.   

### Iteración 2: Capa de Control (PM & Tutor) 🏗️
- **Estado:** Completada.
- **Descripción:** Experimentación con la definición y colaboración de un Agente Project Manager y un Agente Tutor para la generación de un plan de aprendizaje inicial sobre IA Agéntica, validando sus roles y la interacción básica.
- **Hitos:**
  - Implementar el **Project Manager Agent** (ejecución y backlog).
  - Implementar el **Tutor Agent** (teoría y "Deep Dives").
  - Generación del primer *Learning Path* oficial basado en los requisitos.
- **Aprendizajes Clave:** 
  - Diseño de agentes especializados con `role`, `goal`, `backstory`. 
  - Orquestación de colaboración `sequential` entre agentes. 
  - Ingeniería de prompts para mejorar la interacción. Comprensión de la arquitectura básica de CrewAI (Agent, Task, Crew, process).

---

## 🚀 Roadmap (Próximas Etapas)

### Iteración 3: Herramientas de Acción (Search & File Read) ⏳
- **Objetivo:** Dotar a los agentes de capacidades de búsqueda (Serper) y lectura de documentos locales.

### Iteración 4: Motor de Ideas (Scout & Refiner) ⏳
- **Objetivo:** Automatizar la propuesta y validación de proyectos de aprendizaje (considerando hardware y redundancia).

### Iteración 5: Inteligencia Híbrida (Ollama) ⏳
- **Objetivo:** Integración de modelos locales para tareas de soporte, testing y QA.

### Iteración 6: Persistencia y Evolución ⏳
- **Objetivo:** Implementar memoria a largo plazo (ChromaDB/LanceDB) para que el sistema aprenda de iteraciones pasadas.

---
*Última actualización: 30 de Marzo, 2026*