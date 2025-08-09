import streamlit as st
import matplotlib.pyplot as plt

st.title("Infografía: Pasos clave en la Auditoría Forense - Caso AgroAndes S.A.")

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

plot_infografia()

