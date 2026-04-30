import streamlit as st
from openai import OpenAI

# 1. Configuración visual de la aplicación
st.set_page_config(page_title="Monitor Vet Pro", page_icon="🐾")
st.title("🐾 Monitor Veterinario Senior")
st.markdown("---")
st.write("Bienvenido al sistema de consulta técnica académica.")

# 2. Tu activo de negocio (La API Key que ya tienes)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 3. Control de Acceso (Tus usuarios autorizados)
# Fuente: User Summary - Relationships
usuarios_autorizados = ["3107153382", "3203328757", "71058449", "83349558"]

# 4. Interfaz de Usuario
telefono = st.text_input("Introduce tu número de celular registrado:", placeholder="Ej: 573...")

if telefono:
    if telefono in usuarios_autorizados:
        st.success(f"✅ Acceso autorizado para el usuario {telefono}")
        
        # Área para que escriban la consulta
        pregunta = st.text_area("Escribe tu consulta técnica o académica (fármacos, dosis, patologías):")
        
        if st.button("Consultar Monitor"):
            if pregunta:
                with st.spinner("Buscando respuesta técnica profesional..."):
                    try:
                        # Petición a la IA (gpt-4o-mini para optimizar tus $3.5 USD)
                        completion = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": "Eres un Monitor Senior de Veterinaria. Responde de forma técnica, estructurada y bilingüe si es necesario."},
                                {"role": "user", "content": pregunta}
                            ]
                        )
                        
                        # Mostrar el resultado final en la web
                        st.markdown("### 📋 Respuesta del Monitor:")
                        st.write(completion.choices[0].message.content)
                        
                    except Exception as e:
                        st.error(f"Ocurrió un error técnico: {e}")
            else:
                st.warning("Por favor, ingresa una pregunta antes de consultar.")
    else:
        # Muro de pago/seguridad
        st.error("❌ Número no registrado. Por favor, contacta al administrador para activar tu suscripción.")

# Pie de página profesional
st.markdown("---")
st.caption("Powered by SSG OPS - Monitoría Veterinaria Inteligente")
st.caption("Todos los derechos reservados - 2026")
