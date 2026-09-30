import time
import streamlit as st

st.set_page_config(page_title="Para ti, mi amor", page_icon="💖")

st.title("💻 Cargando programa especial...")

if st.button("Ejecutar sorpresa 🚀"):
  with st.spinner("Analizando sentimientos..."):
    time.sleep(2)

  st.success("¡Sistema inicializado con éxito!")

  st.markdown("---")
  st.subheader("Estado actual:")
  st.code(
      """
    sentimiento = "Amor infinito"
    persona = "Mi novia hermosa"
    conexion = "Para siempre"
    """,
      language="python",
  )

  st.balloons()
  st.markdown(
      """
    <div style='text-align: center;'>
        <h1>❤️ Te amo muchísimo ❤️️</h1>
        <p style='font-size: 20px;'>Eres lo mejor que me ha pasado en la vida entera.</p>
    </div>
    """,
     unsafe_allow_html=True
