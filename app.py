#app.py
#git remote set-url origin 
#git push origin main
# frontend/app.py
#ESTE ES EL CONTROLADOR PRINCIPAL DE LA APLICACIÓN
import streamlit as st

# Configuración inicial
st.set_page_config(page_title="LuxBeauty Lab", layout="wide")

# Menú lateral
st.sidebar.markdown("## 💠 LUXBEAUTY LAB")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navegación",
    [
        "Gestión de clientes",
        "Gestión de servicios",
        "Gestión de inventarios",
        "Reportes",
        "Facturación",
        "Cuadre de caja",
        "Solicitar Soporte",
        "Seguridad y Accesos"
    ],
    label_visibility="collapsed"
)

# Botón de configuración
st.sidebar.markdown("---")
st.sidebar.button("⚙️ CONFIGURACIÓN")

#Importación dinámica según selección
if menu == "Gestión de clientes":
    import secciones.clientes as clientes
    clientes.pantalla_clientes()

#elif menu == "Gestión de servicios":
#    import secciones.servicios as servicios
#    servicios.pantalla_servicios()
#
#elif menu == "Gestión de inventarios":
#    import secciones.inventario as inventario
#    inventario.pantalla_inventario()
#
elif menu == "Reportes":
    import secciones.reportes as reportes
    reportes.pantalla_reportes()

#elif menu == "Facturación":
#    import secciones.facturacion as facturacion
#    facturacion.pantalla_facturacion()

#elif menu == "Cuadre de caja":
#    import secciones.caja as caja
#    caja.pantalla_caja()

#elif menu == "Solicitar Soporte":
#    import secciones.soporte as soporte
#    soporte.pantalla_soporte()

#elif menu == "Seguridad y Accesos":
 #   import secciones.seguridad as seguridad
#    seguridad.pantalla_seguridad()