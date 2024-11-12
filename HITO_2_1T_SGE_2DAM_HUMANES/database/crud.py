# En primer lugar importo los módulos necesarios para mi programa
import os
import sys
# Añado el directorio raíz del proyecto al path de Python cuando ejecuto este archivo directamente
if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importo los tipos y clases que voy a necesitar
from typing import List, Optional
from mysql.connector import Error
from models.survey import Survey
from database.connection import DBConnection

# Creo mi clase SurveyDAO que se encargará de todas las operaciones con la base de datos
class SurveyDAO:
    def __init__(self):
        # Inicio mi conexión a la base de datos
        self.db = DBConnection()

    def create(self, survey: Survey) -> bool:
        # En este método implemento la creación de una nueva encuesta
        # Uso try-except para manejar posibles errores en la base de datos
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = """INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, 
                    BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, 
                    DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                survey.idEncuesta, survey.edad, survey.Sexo,
                survey.BebidasSemana, survey.CervezasSemana,
                survey.BebidasFinSemana, survey.BebidasDestiladasSemana,
                survey.VinosSemana, survey.PerdidasControl,
                survey.DiversionDependenciaAlcohol, survey.ProblemasDigestivos,
                survey.TensionAlta, survey.DolorCabeza
            )
            cursor.execute(sql, values)
            conn.commit()
            return True
        except Error as e:
            print(f"Error creating survey: {e}")
            return False
        finally:
            cursor.close()

    def read_all(self) -> List[Survey]:
        # Este método me permite obtener todas las encuestas de la base de datos
        # Devuelvo una lista de objetos Survey
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM ENCUESTA")
            results = cursor.fetchall()
            return [Survey(**result) for result in results]
        except Error as e:
            print(f"Error reading surveys: {e}")
            return []
        finally:
            cursor.close()

    def read_by_id(self, survey_id: int) -> Optional[Survey]:
        # Con este método busco una encuesta específica por su ID
        # Puede devolver None si no encuentra la encuesta
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM ENCUESTA WHERE idEncuesta = %s", (survey_id,))
            result = cursor.fetchone()
            return Survey(**result) if result else None
        except Error as e:
            print(f"Error reading survey: {e}")
            return None
        finally:
            cursor.close()

    def update(self, survey: Survey) -> bool:
        # Aquí actualizo los datos de una encuesta existente
        # Devuelvo True si la actualización fue exitosa
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = """UPDATE ENCUESTA SET 
                    edad = %s, Sexo = %s, BebidasSemana = %s,
                    CervezasSemana = %s, BebidasFinSemana = %s,
                    BebidasDestiladasSemana = %s, VinosSemana = %s,
                    PerdidasControl = %s, DiversionDependenciaAlcohol = %s,
                    ProblemasDigestivos = %s, TensionAlta = %s,
                    DolorCabeza = %s
                    WHERE idEncuesta = %s"""
            values = (
                survey.edad, survey.Sexo, survey.BebidasSemana,
                survey.CervezasSemana, survey.BebidasFinSemana,
                survey.BebidasDestiladasSemana, survey.VinosSemana,
                survey.PerdidasControl, survey.DiversionDependenciaAlcohol,
                survey.ProblemasDigestivos, survey.TensionAlta,
                survey.DolorCabeza, survey.idEncuesta
            )
            cursor.execute(sql, values)
            conn.commit()
            return True
        except Error as e:
            print(f"Error updating survey: {e}")
            return False
        finally:
            cursor.close()

    def delete(self, survey_id: int) -> bool:
        # Este método elimina una encuesta de la base de datos
        # Solo necesito el ID para eliminar
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta = %s", (survey_id,))
            conn.commit()
            return True
        except Error as e:
            print(f"Error deleting survey: {e}")
            return False
        finally:
            cursor.close()

    def get_by_filters(self, filters: dict) -> List[Survey]:
        # Este es un método más avanzado que me permite buscar encuestas con filtros
        # Recibo un diccionario con los filtros a aplicar
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            
            conditions = []
            values = []
            for key, value in filters.items():
                conditions.append(f"{key} = %s")
                values.append(value)
                
            where_clause = " AND ".join(conditions)
            sql = f"SELECT * FROM ENCUESTA WHERE {where_clause}"
            
            cursor.execute(sql, tuple(values))
            results = cursor.fetchall()
            return [Survey(**result) for result in results]
        except Error as e:
            print(f"Error filtering surveys: {e}")
            return []
        finally:
            cursor.close()