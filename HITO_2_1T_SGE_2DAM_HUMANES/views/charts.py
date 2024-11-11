import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database.crud import SurveyDAO

def plot_consumption_by_age(chart_frame):
    dao = SurveyDAO()
    surveys = dao.read_all()
    df = pd.DataFrame([(s.edad, s.BebidasSemana) for s in surveys], 
                      columns=['Edad', 'Consumo'])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='scatter', x='Edad', y='Consumo', ax=ax)
    ax.set_title('Consumo de Alcohol por Edad')
    
    canvas = FigureCanvasTkAgg(fig, chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

def plot_health_problems(chart_frame):
    # Limpiar el frame
    for widget in chart_frame.winfo_children():
        widget.destroy()

    dao = SurveyDAO()
    surveys = dao.read_all()
    
    # Crear DataFrame con valores binarios
    data = pd.DataFrame([{
        'ProblemasDigestivos': 1 if str(s.ProblemasDigestivos).lower() in ['1', 'si', 'sí', 'true', 'yes'] else 0,
        'TensionAlta': 1 if str(s.TensionAlta).lower() in ['1', 'si', 'sí', 'true', 'yes'] else 0,
        'DolorCabeza': 1 if str(s.DolorCabeza).lower() in ['1', 'si', 'sí', 'true', 'yes'] else 0
    } for s in surveys])
    
    # Calcular totales de cada problema
    totals = {
        'Problemas Digestivos': data['ProblemasDigestivos'].sum(),
        'Tensión Alta': data['TensionAlta'].sum(),
        'Dolor de Cabeza': data['DolorCabeza'].sum()
    }
    
    # Crear figura
    plt.clf()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    # Gráfico circular
    valores = list(totals.values())
    etiquetas = list(totals.keys())
    
    # Añadir porcentajes a las etiquetas
    total_casos = sum(valores)
    etiquetas = [f'{label}\n({value/total_casos*100:.1f}%)' 
                 for label, value in zip(etiquetas, valores)]
    
    # Crear gráfico circular con colores específicos
    colores = ['#E94560', '#16213E', '#0F3460']  # Rosa neón, Azul medianoche, Azul real
    wedges, texts, autotexts = ax1.pie(valores, 
                                      labels=etiquetas,
                                      colors=colores,
                                      autopct='%1.1f%%',
                                      startangle=90)
    
    # Añadir título y leyenda
    ax1.set_title('Distribución de Problemas de Salud')
    
    # Crear gráfico de barras complementario
    problemas = list(totals.keys())
    cantidades = list(totals.values())
    
    ax2.bar(problemas, cantidades, color=colores)
    ax2.set_title('Cantidad de Casos por Problema')
    ax2.set_ylabel('Número de Casos')
    plt.xticks(rotation=45)
    
    # Ajustar layout
    plt.style.use('dark_background')
    fig.patch.set_facecolor('#1A1A2E')  # Fondo oscuro
    ax1.set_facecolor('#1A1A2E')
    ax2.set_facecolor('#1A1A2E')
    plt.tight_layout()
    
    # Mostrar en tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')
