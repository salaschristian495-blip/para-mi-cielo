import time
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Para ti, mi amor ❤", page_icon="💖")

# Estilo y diseño romántico
st.markdown(
    """
    <style>
    .main {
        background-color: #fff0f5;
    }
    h1 {
        color: #d81b60;
        text-align: center;
    }
    .subtext {
        text-align: center;
        font-size: 18px;
        color: #ad1457;
    }
    .counter-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Para la persona más especial de mi vida 💖")
st.markdown(
    "<p class='subtext'>Hice este pequeño detalle digital solo para recordarte"
    " lo mucho que te amo, Yaya.</p>",
    unsafe_allow_html=True,
)

st.markdown("---")

# Fecha de inicio: 25 de julio de 2026
inicio_relacion = datetime(2026, 7, 25, 0, 0, 0)
ahora = datetime.now()

# Cálculo del tiempo transcurrido
diferencia = ahora - inicio_relacion
dias = diferencia.days
segundos_totales = int(diferencia.total_seconds())
horas = (segundos_totales % 86400) // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

# Mostrar el contador en pantalla
st.markdown("### ⏳ Nuestro tiempo juntos desde el 25 de julio de 2026:")
col1, col2, col3, col4 = st.columns(4)
with col1:
  st.metric("Días", dias)
with col2:
  st.metric("Horas", horas)
with col3:
  st.metric("Minutos", minutos)
with col4:
  st.metric("Segundos", segundos)

st.markdown("---")

# Sección interactiva
if st.button("Haz clic aquí para una sorpresa 💌"):
  with st.spinner("Abriendo mi corazón..."):
    time.sleep(1.5)

  st.success("¡Mensaje entregado con éxito!")
  st.balloons()

  st.markdown("""
    ### Mi amor,
    Quiero agradecerte por cada risa, por cada momento a tu lado y por ser 
    la luz de mis días. No importa la distancia ni lo ocupado que esté el día, 
    tú siempre estás en mi mente y en mi corazón.

    Eres lo mejor que me ha pasado, mi compañera y mi más grande inspiración. 
    Te amo con todo lo que soy.
    """)

  st.markdown(
      "<h2 style='text-align: center; color: #e91e63;'>¡Eres mi todo, Yaya!"
      " ❤️</h2>",
      unsafe_allow_html=True,
  )

# Truco para que la página se actualice sola cada segundo y corra el contador
time.sleep(1)
st.rerun()
