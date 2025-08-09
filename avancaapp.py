import streamlit as st
import matplotlib.pyplot as plt
from graphviz import Digraph

st.set_page_config(page_title="Auditoría Forense - AgroAndes", layout="wide")

st.title("Auditoría Forense - Caso AgroAndes S.A.")

# --- Infografía con matplotlib ---
def plot_infografia():
    steps = [
        "1. Reunión inicial con gerencia",
        "2. Evaluación preliminar de riesgos",
        "3. Recopilación y revisión documental",
        "4. Análisis de nómina y registros bancarios",
        "5. Verificación presencial y entrevistas",
        "6. Análisis forense digital",
        "7. Informe final y recomendaciones"
    ]
    fig, ax = plt.subplots(figsize=(10,6))
    ax.axis('off')
    y_pos = list(range(len(steps), 0, -1))
    for i, step in enumerate(steps):
        ax.text(0.05, y_pos[i]/10, step, fontsize=12, ha='left', va='center',
                bbox=dict(boxstyle="round,pad=0.5", fc="#8ecae6", ec="b", lw=2))
        if i < len(steps) - 1:
            ax.annotate("", xy=(0.5, y_pos[i+1]/10 + 0.03), xytext=(0.5, y_pos[i]/10 - 0.03),
                        arrowprops=dict(arrowstyle="->", color="black", lw=2))
    plt.title("Infografía: Pasos clave en la Auditoría Forense AgroAndes S.A.", fontsize=14)
    st.pyplot(fig)

# --- Mapa Mental con graphviz ---
def render_mapa_mental():
    dot = Digraph(comment='Mapa Mental Auditoría Forense AgroAndes')

    dot.node('A', 'Auditoría Forense')
    dot.node('B', 'Evaluación de Riesgos')
    dot.node('C', 'Análisis Documental')
    dot.node('D', 'Investigación Física')
    dot.node('E', 'Análisis Digital')
    dot.node('F', 'Entrevistas')
    dot.node('G', 'Informe Final')

    dot.edges(['AB', 'AC', 'AD', 'AE', 'AF'])
    dot.edge('A', 'G')

    # Guardar imagen en temporal y mostrar
    file_path = "mapa_mental_auditoria_forense"
    dot.render(file_path, format='png', cleanup=True)
    st.image(file_path + ".png", caption='Mapa Mental Auditoría Forense')

# --- Main ---
st.header("Infografía de Pasos de Auditoría")
plot_infografia()

st.header("Mapa Mental de Auditoría Forense")
render_mapa_mental()
