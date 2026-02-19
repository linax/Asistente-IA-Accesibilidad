import streamlit as st
from google import genai
from google.genai import types

# 1. Configuración de la interfaz
st.set_page_config(page_title="Asistente Accesibilidad Chile", page_icon="♿")
st.markdown("""
    <style>
       
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
st.title("♿ Asistente de Derechos y Accesibilidad")
st.markdown("Orientación legal y técnica basada en la normativa chilena vigente.")

# 2. Cargar el conocimiento (Las Leyes)
@st.cache_data
def cargar_normativa():
    try:
        with open("normativa_chile.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: No se encontró el archivo normativa_chile.md"

contexto_legal = cargar_normativa()

# 3. Autenticación segura
# En Streamlit Cloud, agrega GOOGLE_API_KEY en 'Settings > Secrets'
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Por favor, configura la GOOGLE_API_KEY en los secretos de Streamlit.")
    st.stop()

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# 4. Configuración del System Prompt (Multi-persona)
SYSTEM_PROMPT = f"""
Eres el Asistente Experto en Accesibilidad y Derechos de Inclusión en Chile.
Tu misión es orientar a ciudadanos en la defensa de sus derechos y asesorar a instituciones en cumplimiento.

CONTEXTO LEGAL PROPORCIONADO:
{contexto_legal}

REGLAS DE ORO:
1. Si el usuario es una PERSONA/CIUDADANO: Tono empático y enfocado en defensa de derechos. 
   Explica pasos para denunciar (Juzgado de Policía Local, DT o SENADIS).
2. Si el usuario es una INSTITUCIÓN/EMPRESA: Tono técnico y preventivo. 
   Enfócate en medidas exactas, plazos y multas.
3. SIEMPRE cita el artículo o ley (ej: 'Según el Art. 4.1.7 de la OGUC...').
4. Si la info no está en el contexto, di: 'No dispongo de esa especificación técnica en mi base legal actual'.
5. RECHAZA temas no relacionados con inclusión o accesibilidad en Chile.
"""

# 5. Gestión del Historial de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. Lógica de Respuesta
if prompt := st.chat_input("Ej: ¿Cómo denuncio discriminación laboral?"):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta con Gemini
    with st.chat_message("assistant"):
        try:
            # Usamos gemini-2.0-flash para balance entre velocidad y razonamiento legal
            response = client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.2, # Baja temperatura para mayor precisión técnica
                )
            )
            
            full_response = response.text
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Hubo un error con la IA: {e}")

# Pie de página legal
st.divider()
st.caption("Aviso: Este asistente es informativo y no constituye asesoría legal formal.") 