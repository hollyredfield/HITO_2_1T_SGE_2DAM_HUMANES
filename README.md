# HITO_2_1T_SGE_2DAM_HUMANES
HITO INDIVIDUAL SISTEMAS DE GESTIÓN EMPRESARIAL

## 🍷 Sistema de Encuestas de Consumo de Alcohol

## 👋 Sobre mí y el proyecto
Hola, soy HollyRedfield (@hollyredfield), y he desarrollado este sistema para gestionar encuestas sobre consumo de alcohol en una clínica médica.

---

## 📋 Descripción
He creado una aplicación completa con interfaz gráfica que permite gestionar y analizar encuestas sobre consumo de alcohol y sus efectos en la salud. Mi sistema utiliza Python con Tkinter para la interfaz y MySQL para el almacenamiento de datos.

---

## ✨ Características principales que he implementado

### 🖥️ Interfaz de Usuario
- He diseñado una interfaz moderna y amigable usando Tkinter.
- Implementé un sistema de pestañas para organizar la información.
- Agregué efectos visuales y animaciones para mejorar la experiencia del usuario.

### 📊 Gestión de Datos
- Desarrollé operaciones CRUD completas para las encuestas.
- Añadí filtros avanzados para la visualización de datos, incluyendo:
  - Nivel de consumo de alcohol.
  - Edad.
  - Sexo.
  - Problemas de salud relacionados.
- Incluí opciones de ordenamiento por cualquier campo para mejorar la accesibilidad de los datos.

### 📈 Visualización
- Implementé gráficos interactivos usando matplotlib para analizar los datos de manera visual.
- Añadí tipos de gráficos específicos, incluyendo:
  - Consumo por edad (dispersión).
  - Problemas de salud (gráficos circulares y de barras).
- Los gráficos se actualizan en tiempo real para reflejar los datos más recientes.

### 📗 Exportación
- Agregué funcionalidad para exportar los datos a archivos Excel.
- Los datos se exportan con formato adecuado para su lectura en Excel.
- Incluí mensajes de confirmación para mejorar la experiencia del usuario.

---

## 🛠️ Tecnologías que he utilizado
- **Python 3.x**: Lenguaje principal.
- **Tkinter**: Para la interfaz gráfica de usuario.
- **MySQL**: Para la base de datos.
- **Pandas**: Para manejo y análisis de datos.
- **Matplotlib**: Para generación de gráficos.
- **openpyxl**: Para exportación de datos a Excel.

---

## 📥 Instalación (Todo se descarga e instala de forma automática si no se tiene instalado los paquetes necesarios sin problemas, pero en cuyo caso dejo esta anotación)
    
1. Instala los paquetes necesarios desde `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2. Configura la base de datos MySQL:
   ```sql
   CREATE DATABASE encuesta;
   USE encuesta;
Nota: El script SQL completo está en database/schema.sql

🚀 Uso
Para ejecutar la aplicación:
    python main.py
    
📝 Configuración de la Base de Datos
He configurado la conexión en database/connection.py:
        host='localhost'
        user='root'
        password=''
        database='encuesta'

🤝 Contribuciones
Si encuentras algún problema en mi código o tienes sugerencias:

Abre un issue.
Describe el problema o la mejora que propones.
Si es posible, propón una solución detallada.

📄 Licencia
Este proyecto está bajo mi licencia personal (HollyRedfield).

📫 Contacto
Si deseas contactarme para discutir el proyecto o sugerencias:

GitHub: @hollyredfield
🙏 Agradecimientos
Agradezco la oportunidad de desarrollar esta herramienta para su clínica.

⭐ ¡Si te gusta mi proyecto, no dudes en darle una estrella!










    
