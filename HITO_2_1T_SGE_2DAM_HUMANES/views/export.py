# Importo pandas para el manejo de datos tabulares y lo renombro como pd
import pandas as pd
# Importo messagebox de tkinter para mostrar mensajes al usuario
from tkinter import messagebox
# Importo la clase SurveyDAO del módulo crud de la base de datos
from database.crud import SurveyDAO

# Defino una función que exportará los datos a Excel
def export_to_excel():
    # Creo una instancia del objeto de acceso a datos de encuestas
    dao = SurveyDAO()
    # Leo todas las encuestas de la base de datos
    surveys = dao.read_all()
    # Convierto las encuestas a un DataFrame de pandas, transformando cada objeto a diccionario
    df = pd.DataFrame([vars(s) for s in surveys])
    # Guardo el DataFrame en un archivo Excel llamado 'encuestas.xlsx' sin incluir índices
    df.to_excel('encuestas.xlsx', index=False)
    # Muestro un mensaje de éxito al usuario
    messagebox.showinfo("Éxito", "Datos exportados a encuestas.xlsx")
