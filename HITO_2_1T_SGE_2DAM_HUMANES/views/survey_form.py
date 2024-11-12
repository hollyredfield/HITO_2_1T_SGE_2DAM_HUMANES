# Primero importo los módulos necesarios: tkinter para la interfaz, messagebox para los diálogos,
# y las clases necesarias para manejar las encuestas
import tkinter as tk
from tkinter import ttk, messagebox
from database.crud import SurveyDAO
from models.survey import Survey

# En esta clase, he creado el formulario para gestionar las encuestas.
# Uso tkinter.Toplevel para crear una ventana secundaria modal.
class SurveyForm(tk.Toplevel):
    def __init__(self, parent, survey=None):
        # En mi constructor, configuro la ventana con un estilo moderno
        super().__init__(parent)
        self.parent = parent
        self.transient(parent)  # Make window transient to parent
        self.grab_set()  # Make window modal
        self.survey = survey
        self.dao = SurveyDAO()
        # Configurar ventana con estilo Apple
        self.configure(bg='#F5F5F7')
        self.title("Formulario de Encuesta")
        self.geometry("500x600")
        
        # Efectos de sombra y bordes redondeados
        self.attributes("-alpha", 0.0)  # Iniciar invisible para animación
        
        # Center the window
        self.geometry("+%d+%d" % (
            parent.winfo_rootx() + 50,
            parent.winfo_rooty() + 50))
        
        self.setup_ui()
        if survey:
            self.load_survey_data()
        
        # Animación de aparición
        self.animate_window()

    def animate_window(self):
        # He implementado esta función para crear una animación suave al abrir el formulario
        def fade_in():
            alpha = self.attributes("-alpha")
            if alpha < 1.0:
                alpha += 0.1
                self.attributes("-alpha", alpha)
                self.after(20, fade_in)
        fade_in()

    def setup_ui(self):
        # En esta función construyo toda la interfaz de usuario del formulario
        # Primero configuro mis estilos personalizados
        style = ttk.Style()
        
        # Colores exóticos
        FORM_COLORS = {
            'bg': '#1A1A2E',
            'fg': '#E94560',
            'input_bg': '#16213E',
            'input_fg': '#FFFFFF',
            'button': '#E94560',
            'button_hover': '#FF2E63'
        }
        
        self.configure(bg=FORM_COLORS['bg'])
        
        # Estilo para campos de entrada
        style.configure('Form.TEntry',
            fieldbackground=FORM_COLORS['input_bg'],
            foreground=FORM_COLORS['input_fg'],
            borderwidth=2,
            relief='solid',
            padding=10)
        
        # Estilo para etiquetas del formulario
        style.configure('Form.TLabel',
            background=FORM_COLORS['bg'],
            foreground=FORM_COLORS['fg'],
            font=('Helvetica', 10, 'bold'),
            padding=5)
        
        main_frame = ttk.Frame(self, style='Card.TFrame')
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        self.entries = {}
        # Creo una lista de campos que necesito para la encuesta
        fields = ["edad", "Sexo", "BebidasSemana", "CervezasSemana", 
                 "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana",
                 "PerdidasControl", "DiversionDependenciaAlcohol", 
                 "ProblemasDigestivos", "TensionAlta", "DolorCabeza"]
        
        # Para cada campo, creo un frame con su etiqueta y campo de entrada
        for field in fields:
            frame = ttk.Frame(main_frame)
            frame.pack(fill='x', pady=2)
            
            # Display a capitalized version for the label but keep the field name as is
            label = ttk.Label(frame, text=field.capitalize(), width=20)
            label.pack(side='left', padx=5)
            
            entry = ttk.Entry(frame)
            entry.pack(side='left', fill='x', expand=True, padx=5)
            self.entries[field] = entry

        # Aplicar estilos a los campos
        for field, entry in self.entries.items():
            entry.configure(style='Form.TEntry')

        # Añado los botones de guardar y cancelar al final del formulario
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Estilo personalizado para los botones
        style = ttk.Style()
        style.configure('Large.TButton',
            padding=(20, 10),  # (horizontal, vertical)
            font=('Helvetica', 11, 'bold'),
            width=15  # Ancho del botón
        )
        
        save_btn = ttk.Button(button_frame, 
                             text="Guardar", 
                             style='Large.TButton',
                             command=self.save_survey)
        save_btn.pack(side='left', padx=10)
        
        cancel_btn = ttk.Button(button_frame, 
                               text="Cancelar", 
                               style='Large.TButton',
                               command=self.destroy)
        cancel_btn.pack(side='left', padx=10)

    def load_survey_data(self):
        # Esta función la uso para cargar los datos de una encuesta existente en el formulario
        for field, entry in self.entries.items():
            entry.insert(0, getattr(self.survey, field))

    def save_survey(self):
        # Aquí manejo el guardado de la encuesta
        # Primero valido que todos los campos estén llenos
        try:
            data = {}
            for field, entry in self.entries.items():
                value = entry.get().strip()
                if not value:
                    messagebox.showwarning("Error", f"El campo {field} no puede estar vacío")
                    return
                data[field] = value

            # Si es una encuesta existente, la actualizo
            if self.survey:
                # Actualizar encuesta existente
                for key, value in data.items():
                    setattr(self.survey, key, value)
                success = self.dao.update(self.survey)
            else:
                # Si es nueva, genero un nuevo ID y la creo
                # Crear nueva encuesta
                surveys = self.dao.read_all()
                new_id = max([s.idEncuesta for s in surveys]) + 1 if surveys else 1
                data['idEncuesta'] = new_id
                new_survey = Survey(**data)
                success = self.dao.create(new_survey)

            # Muestro un mensaje de éxito y actualizo la vista principal
            if success:
                messagebox.showinfo("Éxito", "Encuesta guardada correctamente")
                self.destroy()
            else:
                # Si algo falla, muestro un error
                messagebox.showerror("Error", "No se pudo guardar la encuesta")
                
        except Exception as e:
            # Capturo cualquier error inesperado y lo muestro
            messagebox.showerror("Error", f"Error al guardar la encuesta: {str(e)}")
