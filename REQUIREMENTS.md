# 🏭 AgentFactory: Hoja de Requisitos del Proyecto (v1.0)

## 1. Visión y Objetivo
**AgentFactory** es un ecosistema de **Agentic AI** diseñado como un laboratorio de aprendizaje iterativo. El objetivo es construir, paso a paso, una "fábrica" de agentes inteligentes que interactúen entre sí y con el usuario para resolver problemas complejos, mientras se dominan las herramientas y arquitecturas de vanguardia de 2025-2026.

---

## 2. Metodología: El Ciclo de Iteración
Se abandona el concepto de "semanas" por el de **Iteraciones**. Cada iteración tiene una duración variable según la complejidad del concepto a aprender y se considera finalizada cuando el usuario domina la técnica implementada.

---

## 3. Arquitectura del Ecosistema

### A. Capa de Dirección y Mentoría (Control)
* **Project Manager Agent (PM):** Asistente personal y coordinador. Gestiona el backlog, define objetivos de la iteración y sugiere mejoras en la arquitectura.
* **Tutor Agent:** Mentor académico. Documenta cada iteración, explica los conceptos técnicos (RAG, Chain of Thought, etc.) y propone ejercicios de profundización ("Deep Dives").

### B. Capa Operativa (Ciclo de Vida)
* **Scout Agent (Explorador):** Rastrea tendencias de IA y propone proyectos que escalen en dificultad.
* **Idea Refiner Agent:** Valida propuestas del Scout mediante un proceso iterativo (máx. N veces). Evalúa factibilidad técnica, hardware y evita redundancias.
* **Coder Agent:** Apoya en la implementación y generación de código siguiendo las mejores prácticas de 2026.
* **QA/Testing Agent:** Diseña y ejecuta pruebas para validar la implementación.

---

## 4. Stack Tecnológico (Tendencia 2026)

| Componente | Tecnología | Uso |
| :--- | :--- | :--- |
| **Modelos Cloud** | Gemini 2.5 Flash / Pro | Razonamiento complejo, PM, Tutor y Refiner. |
| **Modelos Locales** | Ollama (Llama 3.2, Mistral) | Tareas atómicas, testing, privacidad y ahorro de API. |
| **Orquestación** | CrewAI / LangGraph | Gestión de roles, estados y flujos cíclicos. |
| **Persistencia** | ChromaDB / LanceDB | Memoria a largo plazo y evolución del sistema. |
| **Hardware** | Microsoft Surface 2 (16GB RAM) | Entorno de ejecución optimizado (CUDA/DirectML). |

---

## 5. Requisitos Funcionales y Sugerencias de Mejora
* **Hybrid Intelligence:** Balance inteligente entre modelos locales (Ollama) y cloud (Gemini).
* **Persistencia Evolutiva:** El sistema debe "recordar" lecciones pasadas para no repetir errores o conceptos.
* **Evaluador de Alucinaciones:** El agente de QA debe verificar la veracidad del código y sugerencias.
* **Human-in-the-Loop:** Puntos de control obligatorios donde el usuario valida el progreso.
* **Dashboard de Control:** (Sugerido) Interfaz local en Streamlit para visualizar el estado de la "fábrica".
* **Errores Didácticos:** (Sugerido) El Tutor puede inyectar retos controlados en el código para forzar el aprendizaje.

---

## 6. Restricciones de Hardware
* **Optimización de RAM:** Los modelos locales no deben superar los 8B-11B de parámetros.
* **Gestión de Contexto:** Uso de *Context Caching* de Gemini para optimizar costes y latencia.

---

> **Última Actualización:** 30 de Marzo, 2026
> **Estado:** Fase de Definición Completada ✅