from datetime import datetime
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Zoëli | Tienda Exclusiva", page_icon="💎", layout="wide"
)

# Inicializar base de datos en session_state para que los cambios persistan
if "productos" not in st.session_state:
  st.session_state.productos = [
      {
          "id": 1,
          "nombre": "Audífonos Inalámbricos Zoëli Pro",
          "categoria": "Tecnología",
          "precio": 899.00,
          "desc": "Cancelación de ruido activa y batería de larga duración.",
          "imagen": None,
      },
      {
          "id": 2,
          "nombre": "Smartwatch Deportivo Elite",
          "categoria": "Tecnología",
          "precio": 1299.00,
          "desc": "Monitoreo de salud avanzado y diseño resistente al agua.",
          "imagen": None,
      },
      {
          "id": 3,
          "nombre": "Mochila Ejecutiva Antirrobo",
          "categoria": "Accesorios",
          "precio": 650.00,
          "desc": "Puerto de carga USB integrado y compartimento seguro.",
          "imagen": None,
      },
  ]

if "carrito" not in st.session_state:
  st.session_state.carrito = []

# --- BARRA LATERAL: NAVEGACIÓN Y ACCESO ---
st.sidebar.title("💎 ZOËLI BOUTIQUE")
modo = st.sidebar.radio(
    "Selecciona el modo:", ["🛍️ Tienda (Comprador)", "⚙️ Panel de Administrador"]
)

# ==========================================
# VISTA 1: COMPRADOR (CLIENTE)
# ==========================================
if modo == "🛍️ Tienda (Comprador)":
  st.title("💎 ZOËLI")
  st.markdown(
      "<h4 style='color: #666; margin-top: -15px;'>Estilo, tecnología y"
      " exclusividad al alcance de un clic.</h4>",
      unsafe_allow_html=True,
  )

  # Carrito en la barra lateral para el comprador
  st.sidebar.markdown("---")
  st.sidebar.subheader("🛒 Tu Carrito")
  if len(st.session_state.carrito) == 0:
    st.sidebar.info("El carrito está vacío.")
  else:
    total_carrito = 0
    for idx, item in enumerate(st.session_state.carrito):
      st.sidebar.write(f"• {item['nombre']} - ${item['precio']:.2f}")
      total_carrito += item["precio"]

    st.sidebar.markdown(f"### **Total: ${total_carrito:.2f} MXN**")

    if st.sidebar.button("🗑️ Vaciar Carrito"):
      st.session_state.carrito = []
      st.rerun()

  # Filtro por Categorías
  categorias = ["Todas"] + list(
      set(p["categoria"] for p in st.session_state.productos)
  )
  categoria_seleccionada = st.selectbox(
      "📁 Filtrar por Categoría", categorias
  )

  # Barra de Búsqueda
  busqueda = st.text_input("🔍 Buscar productos en Zoëli...", "").lower()
  st.markdown("---")

  # Filtrado
  productos_filtrados = st.session_state.productos
  if categoria_seleccionada != "Todas":
    productos_filtrados = [
        p
        for p in productos_filtrados
        if p["categoria"] == categoria_seleccionada
    ]

  if busqueda:
    productos_filtrados = [
        p for p in productos_filtrados if busqueda in p["nombre"].lower()
    ]

  # Mostrar productos
  if len(productos_filtrados) == 0:
    st.warning("No se encontraron productos disponibles.")
  else:
    cols = st.columns(3)
    for index, producto in enumerate(productos_filtrados):
      col = cols[index % 3]
      with col:
        # Contenedor visual del producto
        with st.container():
          if producto["imagen"]:
            st.image(
                producto["imagen"],
                use_container_width=True,
                caption=producto["nombre"],
            )
          else:
            st.markdown(
                "<div"
                " style='font-size: 50px; text-align: center;'>📦</div>",
                unsafe_allow_html=True,
            )

          st.markdown(f"### {producto['nombre']}")
          st.write(producto["desc"])
          st.markdown(
              f"<h4 style='color: #0288d1;'>${producto['precio']:.2f}"
              " MXN</h4>",
              unsafe_allow_html=True,
          )

          if st.button("Agregar al carrito", key=f"comprar_{producto['id']}"):
            st.session_state.carrito.append(producto)
            st.success(f"¡Agregado a Zoëli!")
            st.rerun()

  # Finalizar pedido
  if len(st.session_state.carrito) > 0:
    st.markdown("---")
    st.subheader("📦 Finalizar Compra en Zoëli")
    nombre_cliente = st.text_input("Tu nombre completo:")
    telefono_cliente = st.text_input("Tu número de teléfono / WhatsApp:")

    if st.button("🚀 Confirmar Pedido"):
      if nombre_cliente and telefono_cliente:
        st.success(
            f"¡Muchas gracias por tu compra, {nombre_cliente}! Nos pondremos en"
            f" contacto contigo al número {telefono_cliente} para coordinar el"
            " pago y envío."
        )
        st.balloons()
        st.session_state.carrito = []
      else:
        st.error("Por favor, ingresa tu nombre y teléfono.")

# ==========================================
# VISTA 2: ADMINISTRADOR (CONTROL TOTAL)
# ==========================================
elif modo == "⚙️ Panel de Administrador":
  st.title("⚙️ Panel de Administración - Zoëli")
  st.write(
      "Zona exclusiva para gestionar el inventario, subir nuevos artículos y"
      " controlar la tienda."
  )

  # Control de contraseña simple para proteger el panel
  password = st.text_input(
      "🔑 Contraseña de Administrador:", type="password"
  )

  # Puedes cambiar la contraseña aquí mismo (por defecto es 'admin123')
  if password == "admin123":
    st.success("¡Acceso concedido al panel de control!")
    st.markdown("---")

    st.subheader("➕ Agregar Nuevo Artículo al Catálogo")

    with st.form("form_nuevo_producto", clear_on_submit=True):
      nuevo_nombre = st.text_input("Nombre del Producto")
      nueva_categoria = st.text_input(
          "Categoría (Ej. Tecnología, Accesorios, Hogar)"
      )
      nuevo_precio = st.number_input(
          "Precio (MXN)", min_value=0.0, format="%.2f"
      )
      nueva_desc = st.text_area("Descripción del producto")

      # Sección para subir imagen o tomar foto desde la cámara
      st.markdown("#### 📸 Imagen del Artículo")
      opcion_imagen = st.radio(
          "¿Cómo deseas agregar la foto?",
          ["Subir archivo desde el equipo", "Tomar foto con la cámara"],
      )

      imagen_subida = None
      if opcion_imagen == "Subir archivo desde el equipo":
        imagen_subida = st.file_uploader(
            "Selecciona una imagen", type=["jpg", "png", "jpeg"]
        )
      else:
        imagen_subida = st.camera_input("Toma una foto del artículo")

      submit_button = st.form_submit_button("Publicar Producto en Zoëli")

      if submit_button:
        if nuevo_nombre and nueva_categoria and nuevo_precio > 0:
          nuevo_id = (
              max([p["id"] for p in st.session_state.productos]) + 1
              if st.session_state.productos
              else 1
          )

          st.session_state.productos.append({
              "id": nuevo_id,
              "nombre": nuevo_nombre,
              "categoria": nueva_categoria,
              "precio": nuevo_precio,
              "desc": nueva_desc,
              "imagen": imagen_subida,
          })
          st.success(
              f"¡El producto '{nuevo_nombre}' se ha publicado con éxito en"
              " Zoëli!"
          )
        else:
          st.error("Por favor completa los campos obligatorios y el precio.")

    st.markdown("---")
    st.subheader("📋 Inventario Actual de Productos")
    if len(st.session_state.productos) == 0:
      st.info("No hay productos registrados.")
    else:
      for idx, p in enumerate(st.session_state.productos):
        cols_inv = st.columns([3, 1])
        with cols_inv[0]:
          st.write(
              f"**{p['nombre']}** — {p['categoria']} — **${p['precio']:.2f}**"
          )
        with cols_inv[1]:
          if st.button("🗑️ Eliminar", key=f"del_{p['id']}"):
            st.session_state.productos.pop(idx)
            st.rerun()

  elif password != "":
    st.error("Contraseña incorrecta. (Contraseña de prueba por defecto: admin123)")
