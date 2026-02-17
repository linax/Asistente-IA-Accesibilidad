import google.generativeai as genai
import streamlit as st

# Usa la misma llave que tienes en tu proyecto
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

print("--- LISTA DE MODELOS DISPONIBLES PARA TU CUENTA ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"ID: {m.name} | Pantalla: {m.display_name}")
except Exception as e:
    print(f"Error al listar: {e}")


    """--- LISTA DE MODELOS DISPONIBLES PARA TU CUENTA (Febrero 2026) ---
ID: models/gemini-2.5-flash | Pantalla: Gemini 2.5 Flash
ID: models/gemini-2.5-pro | Pantalla: Gemini 2.5 Pro
ID: models/gemini-2.0-flash | Pantalla: Gemini 2.0 Flash
ID: models/gemini-2.0-flash-001 | Pantalla: Gemini 2.0 Flash 001
ID: models/gemini-2.0-flash-exp-image-generation | Pantalla: Gemini 2.0 Flash (Image Generation) Experimental
ID: models/gemini-2.0-flash-lite-001 | Pantalla: Gemini 2.0 Flash-Lite 001
ID: models/gemini-2.0-flash-lite | Pantalla: Gemini 2.0 Flash-Lite
ID: models/gemini-exp-1206 | Pantalla: Gemini Experimental 1206
ID: models/gemini-2.5-flash-preview-tts | Pantalla: Gemini 2.5 Flash Preview TTS
ID: models/gemini-2.5-pro-preview-tts | Pantalla: Gemini 2.5 Pro Preview TTS
ID: models/gemma-3-1b-it | Pantalla: Gemma 3 1B
ID: models/gemma-3-4b-it | Pantalla: Gemma 3 4B
ID: models/gemma-3-12b-it | Pantalla: Gemma 3 12B
ID: models/gemma-3-27b-it | Pantalla: Gemma 3 27B
ID: models/gemma-3n-e4b-it | Pantalla: Gemma 3n E4B
ID: models/gemma-3n-e2b-it | Pantalla: Gemma 3n E2B
ID: models/gemini-flash-latest | Pantalla: Gemini Flash Latest
ID: models/gemini-flash-lite-latest | Pantalla: Gemini Flash-Lite Latest
ID: models/gemini-pro-latest | Pantalla: Gemini Pro Latest
ID: models/gemini-2.5-flash-lite | Pantalla: Gemini 2.5 Flash-Lite
ID: models/gemini-2.5-flash-image | Pantalla: Nano Banana
ID: models/gemini-2.5-flash-preview-09-2025 | Pantalla: Gemini 2.5 Flash Preview Sep 2025
ID: models/gemini-2.5-flash-lite-preview-09-2025 | Pantalla: Gemini 2.5 Flash-Lite Preview Sep 2025
ID: models/gemini-3-pro-preview | Pantalla: Gemini 3 Pro Preview
ID: models/gemini-3-flash-preview | Pantalla: Gemini 3 Flash Preview
ID: models/gemini-3-pro-image-preview | Pantalla: Nano Banana Pro
ID: models/nano-banana-pro-preview | Pantalla: Nano Banana Pro
ID: models/gemini-robotics-er-1.5-preview | Pantalla: Gemini Robotics-ER 1.5 Preview
ID: models/gemini-2.5-computer-use-preview-10-2025 | Pantalla: Gemini 2.5 Computer Use Preview 10-2025
ID: models/deep-research-pro-preview-12-2025 | Pantalla: Deep Research Pro Preview (Dec-12-2025)"""