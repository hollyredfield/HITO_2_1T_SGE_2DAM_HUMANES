# He creado esta clase Survey para modelar los datos de las encuestas sobre consumo de alcohol.
# La utilizo como un modelo de datos que mapea directamente con mi base de datos.
class Survey:
    # He definido el constructor de mi clase con todos los campos que necesito para la encuesta.
    # Cada parámetro representa una columna diferente en mi tabla de la base de datos.
    def __init__(self, idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, 
                 BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, 
                 PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, 
                 TensionAlta, DolorCabeza):
        # Aquí asigno cada parámetro recibido a su correspondiente atributo de la clase
        # Estos atributos los uso luego para acceder a los datos de cada encuesta
        self.idEncuesta = idEncuesta                    # Identificador único de la encuesta
        self.edad = edad                                # Edad del encuestado
        self.Sexo = Sexo                               # Sexo del encuestado
        self.BebidasSemana = BebidasSemana             # Número total de bebidas por semana
        self.CervezasSemana = CervezasSemana           # Consumo semanal de cervezas
        self.BebidasFinSemana = BebidasFinSemana       # Bebidas consumidas en fin de semana
        self.BebidasDestiladasSemana = BebidasDestiladasSemana  # Consumo de bebidas destiladas
        self.VinosSemana = VinosSemana                 # Consumo semanal de vinos
        self.PerdidasControl = PerdidasControl          # Indica si ha tenido pérdidas de control
        self.DiversionDependenciaAlcohol = DiversionDependenciaAlcohol  # Relación diversión-alcohol
        self.ProblemasDigestivos = ProblemasDigestivos # Problemas digestivos relacionados
        self.TensionAlta = TensionAlta                 # Problemas de tensión alta
        self.DolorCabeza = DolorCabeza                 # Frecuencia de dolores de cabeza