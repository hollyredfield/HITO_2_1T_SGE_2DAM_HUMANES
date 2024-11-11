# views/main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from database.crud import SurveyDAO
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from views.survey_form import SurveyForm
from views.export import export_to_excel
from views.charts import plot_consumption_by_age, plot_health_problems

class MainWindow(ttk.Frame):  # Change to inherit from ttk.Frame
    def __init__(self, root):
        self.setup_styles()  # Configurar el estilo antes de inicializar
        super().__init__(root)  # Initialize parent class
        self.root = root
        self.root.title("Encuesta de Consumo de Alcohol")
        self.root.geometry("1200x800")
        self.dao = SurveyDAO()
        
        self.pack(fill='both', expand=True)  # Pack the frame
        self.setup_ui()
        self.load_data()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Paleta de colores exóticos
        COLORS = {
            'bg': '#1A1A2E',  # Azul oscuro profundo
            'fg': '#E94560',  # Rosa neón
            'accent': '#16213E',  # Azul medianoche
            'text': '#FFFFFF',  # Blanco
            'highlight': '#0F3460',  # Azul real
            'button': '#E94560',  # Rosa neón
            'button_hover': '#FF2E63',  # Rosa brillante
            'tree_bg': '#16213E',  # Azul medianoche
            'tree_selected': '#E94560'  # Rosa neón
        }
        
        # Configuración general
        style.configure('.',
            background=COLORS['bg'],
            foreground=COLORS['text'],
            font=('Helvetica', 10))
        
        # Botones con efecto neón
        style.configure('Accent.TButton',
            background=COLORS['button'],
            foreground=COLORS['text'],
            padding=(20, 10),
            font=('Helvetica', 10, 'bold'))
        
        style.map('Accent.TButton',
            background=[('active', COLORS['button_hover'])],
            foreground=[('active', COLORS['text'])])
        
        # Treeview con estilo cyberpunk
        style.configure('Treeview',
            background=COLORS['tree_bg'],
            foreground=COLORS['text'],
            fieldbackground=COLORS['tree_bg'],
            rowheight=30)
        
        style.map('Treeview',
            background=[('selected', COLORS['tree_selected'])],
            foreground=[('selected', COLORS['text'])])
        
        style.configure('Treeview.Heading',
            background=COLORS['accent'],
            foreground=COLORS['text'],
            font=('Helvetica', 10, 'bold'))
        
        # Pestañas con estilo futurista
        style.configure('TNotebook',
            background=COLORS['bg'],
            tabmargins=[2, 5, 2, 0])
        
        style.configure('TNotebook.Tab',
            background=COLORS['accent'],
            foreground=COLORS['text'],
            padding=(20, 8),
            font=('Helvetica', 10))
        
        style.map('TNotebook.Tab',
            background=[('selected', COLORS['highlight'])],
            expand=[('selected', [1, 1, 1, 0])])
        
        # Frames con bordes brillantes
        style.configure('Card.TFrame',
            background=COLORS['accent'],
            relief='solid',
            borderwidth=1)
        
        # Etiquetas con estilo neón
        style.configure('Neon.TLabel',
            background=COLORS['bg'],
            foreground=COLORS['fg'],
            font=('Helvetica', 11, 'bold'))

    def setup_ui(self):
        self.configure(style='Card.TFrame', padding=20)
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)

        # Data tab
        self.data_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.data_tab, text="Datos")
        self.setup_data_tab()

        # Charts tab
        self.charts_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.charts_tab, text="Gráficos")
        self.setup_charts_tab()

    def setup_data_tab(self):
        # Controls frame
        controls_frame = ttk.LabelFrame(self.data_tab, text="Controles", padding=5)
        controls_frame.pack(fill='x', padx=5, pady=5)

        # Add buttons
        ttk.Button(controls_frame, text="Nuevo", command=self.add_survey).pack(side='left', padx=5)
        ttk.Button(controls_frame, text="Editar", command=self.edit_survey).pack(side='left', padx=5)
        ttk.Button(controls_frame, text="Eliminar", command=self.delete_survey).pack(side='left', padx=5)
        ttk.Button(controls_frame, text="Exportar a Excel", command=self.export_to_excel).pack(side='left', padx=5)

        # Filter frame
        filter_frame = ttk.LabelFrame(self.data_tab, text="Filtros", padding=5)
        filter_frame.pack(fill='x', padx=5, pady=5)

        # Add filter controls
        ttk.Label(filter_frame, text="Sexo:").pack(side='left', padx=5)
        self.sex_filter = ttk.Combobox(filter_frame, values=['Todos', 'Hombre', 'Mujer'])
        self.sex_filter.pack(side='left', padx=5)
        self.sex_filter.set('Todos')

        # Add new filter for consumption
        ttk.Label(filter_frame, text="Consumo:").pack(side='left', padx=5)
        self.consumo_filter = ttk.Combobox(filter_frame, 
            values=['Todos', 'Alto (>10)', 'Medio (5-10)', 'Bajo (<5)'])
        self.consumo_filter.pack(side='left', padx=5)
        self.consumo_filter.set('Todos')

        ttk.Button(filter_frame, text="Aplicar Filtros", command=self.apply_filters).pack(side='left', padx=5)

        # Treeview
        self.tree = ttk.Treeview(self.data_tab)
        self.tree["columns"] = ("ID", "Edad", "Sexo", "BebidasSemana", 
                              "CervezasSemana", "BebidasFinSemana", 
                              "BebidasDestiladasSemana", "VinosSemana",
                              "PerdidasControl", "DiversionDependenciaAlcohol", 
                              "ProblemasDigestivos", "TensionAlta", "DolorCabeza")

        # Configure columns
        self.tree.column("#0", width=0, stretch=tk.NO)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=100)
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_treeview(c))

        self.tree.pack(expand=True, fill='both', padx=5, pady=5)

    def setup_charts_tab(self):
        # Controls for charts
        controls_frame = ttk.Frame(self.charts_tab)
        controls_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(controls_frame, text="Tipo de Gráfico:").pack(side='left', padx=5)
        self.chart_type = ttk.Combobox(controls_frame, 
                                      values=['Consumo por Edad', 'Problemas de Salud'])
        self.chart_type.pack(side='left', padx=5)
        self.chart_type.set('Consumo por Edad')

        ttk.Button(controls_frame, text="Generar Gráfico", 
                  command=self.generate_chart).pack(side='left', padx=5)

        # Frame for chart
        self.chart_frame = ttk.Frame(self.charts_tab)
        self.chart_frame.pack(expand=True, fill='both', padx=5, pady=5)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        surveys = self.dao.read_all()
        for survey in surveys:
            self.tree.insert("", "end", values=(
                survey.idEncuesta, survey.edad, survey.Sexo,
                survey.BebidasSemana, survey.CervezasSemana,
                survey.BebidasFinSemana, survey.BebidasDestiladasSemana, 
                survey.VinosSemana, survey.PerdidasControl,
                survey.DiversionDependenciaAlcohol, survey.ProblemasDigestivos,
                survey.TensionAlta, survey.DolorCabeza
            ))

    def generate_chart(self):
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        if self.chart_type.get() == 'Consumo por Edad':
            plot_consumption_by_age(self.chart_frame)
        else:
            plot_health_problems(self.chart_frame)

    def export_to_excel(self):
        try:
            try:
                import openpyxl
            except ImportError:
                messagebox.showerror("Error", "Por favor, instale openpyxl usando: pip install openpyxl")
                return

            file_path = filedialog.asksaveasfilename(
                defaultextension='.xlsx',
                filetypes=[("Excel files", "*.xlsx")],
                title="Guardar como Excel"
            )
            
            if file_path:
                export_to_excel(self.tree, file_path)
                messagebox.showinfo("Exportación Exitosa", "Los datos han sido exportados a Excel.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")

    def apply_filters(self):
        sex = self.sex_filter.get()
        consumo = self.consumo_filter.get()

        surveys = self.dao.read_all()
        filtered_surveys = []

        for survey in surveys:
            matches_sex = (sex == "Todos" or survey.Sexo == sex)
            consumo_val = survey.BebidasSemana + survey.CervezasSemana + \
                          survey.BebidasFinSemana + survey.BebidasDestiladasSemana + \
                          survey.VinosSemana

            if consumo == "Alto (>10)" and consumo_val <= 10:
                matches_consumo = False
            elif consumo == "Medio (5-10)" and (consumo_val < 5 or consumo_val > 10):
                matches_consumo = False
            elif consumo == "Bajo (<5)" and consumo_val >= 5:
                matches_consumo = False
            else:
                matches_consumo = True

            if matches_sex and matches_consumo:
                filtered_surveys.append(survey)

        self.tree.delete(*self.tree.get_children())
        for survey in filtered_surveys:
            self.tree.insert("", "end", values=(
                survey.idEncuesta, survey.edad, survey.Sexo,
                survey.BebidasSemana, survey.CervezasSemana,
                survey.BebidasFinSemana, survey.BebidasDestiladasSemana,
                survey.VinosSemana, survey.PerdidasControl,
                survey.DiversionDependenciaAlcohol, survey.ProblemasDigestivos,
                survey.TensionAlta, survey.DolorCabeza
            ))

    def add_survey(self):
        SurveyForm(self.root, self)

    def edit_survey(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Encuesta", "Seleccione una encuesta para editar.")
            return

        values = self.tree.item(selected_item)["values"]
        survey_id = values[0]
        SurveyForm(self.root, self, survey_id)

    def delete_survey(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Encuesta", "Seleccione una encuesta para eliminar.")
            return

        values = self.tree.item(selected_item)["values"]
        survey_id = values[0]
        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar esta encuesta?")
        if confirm:
            self.dao.delete(survey_id)
            self.load_data()

    def sort_treeview(self, col):
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
        data.sort(reverse=True)

        for index, (val, child) in enumerate(data):
            self.tree.move(child, '', index)

        self.tree.heading(col, command=lambda: self.sort_treeview(col))
