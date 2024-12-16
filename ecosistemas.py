import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial del tablero
st.set_page_config(
    page_title="Tablero de Control - Ecosistemas Colaborativos y Más",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Títulos principales
st.title("Tablero de Control: Monitoreo Estratégico de OKRs y KPIs")
st.markdown("Este tablero permite al Consejo de Administración monitorear los avances estratégicos en los pivotes clave: **Ecosistemas Colaborativos**, **Alineación Dinámica**, y **Cultura y Liderazgo Digital**.")

# Información inicial
st.sidebar.header("Información de Contexto")
st.sidebar.markdown("""
- **Pivote 1: Ecosistemas Colaborativos**: Mejora de procesos mediante la integración de tecnología y colaboración estratégica.
- **Pivote 2: Alineación Dinámica**: Adaptación estratégica continua en función del entorno cambiante.
- **Pivote 3: Cultura y Liderazgo Digital**: Fomento de habilidades de liderazgo y metodologías ágiles.
""")

# Datos simulados
# Datos sobre los talleres y plantas implementadas para Ecosistemas Colaborativos
data_talleres = pd.DataFrame({
    'Mes': ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    'Talleres Realizados': [1, 3, 2, 4, 2, 5]
})

data_gemelos = pd.DataFrame({
    'Planta': ["Planta 1", "Planta 2", "Planta 3", "Planta 4"],
    'Implementación (%)': [25, 50, 75, 100]
})

# Datos para Alineación Dinámica
satisfaccion_clientes = pd.DataFrame({
    'Trimestre': ["Q1", "Q2", "Q3", "Q4"],
    'Nivel de Satisfacción (%)': [70, 75, 80, 85]
})

# Datos para Cultura y Liderazgo Digital
capacitaciones = pd.DataFrame({
    'Estado': ["Capacitados", "Pendientes"],
    'Porcentaje': [60, 40]
})

# Gráficos y visualización
# Sección Ecosistemas Colaborativos
st.header("Pivote: Ecosistemas Colaborativos")
st.subheader("Avances en talleres realizados")
grafico_talleres = px.bar(data_talleres, x='Mes', y='Talleres Realizados', title="Evolución de Talleres con Startups", color_discrete_sequence=['#636EFA'])
st.plotly_chart(grafico_talleres, use_container_width=True)

st.subheader("Progreso en la implementación de Gemelos Digitales")
grafico_gemelos = px.bar(data_gemelos, x='Planta', y='Implementación (%)', title="Porcentaje de Implementación por Planta", color_discrete_sequence=['#EF553B'])
st.plotly_chart(grafico_gemelos, use_container_width=True)

# Sección Alineación Dinámica
st.header("Pivote: Alineación Dinámica")
st.subheader("Satisfacción del cliente tras ajustes estratégicos")
grafico_satisfaccion = px.line(satisfaccion_clientes, x='Trimestre', y='Nivel de Satisfacción (%)', title="Niveles de Satisfacción por Trimestre", markers=True, color_discrete_sequence=['#00CC96'])
st.plotly_chart(grafico_satisfaccion, use_container_width=True)

# Sección Cultura y Liderazgo Digital
st.header("Pivote: Cultura y Liderazgo Digital")
st.subheader("Progreso en capacitaciones de liderazgo")
grafico_capacitaciones = px.pie(capacitaciones, names='Estado', values='Porcentaje', title="Porcentaje de Líderes Capacitados")
st.plotly_chart(grafico_capacitaciones, use_container_width=True)

# Notas y conclusiones
st.markdown("""
---
### Resumen del Tablero

**Ecosistemas Colaborativos:**
- Talleres realizados para identificar oportunidades tecnológicas.
- Implementación progresiva de gemelos digitales en plantas globales.

**Alineación Dinámica:**
- Mejoras constantes en los niveles de satisfacción del cliente.

**Cultura y Liderazgo Digital:**
- Incremento en el porcentaje de líderes capacitados en metodologías ágiles.

Este tablero refleja el progreso de cada iniciativa y permite al Consejo de Administración tomar decisiones informadas y estratégicas.
""")
