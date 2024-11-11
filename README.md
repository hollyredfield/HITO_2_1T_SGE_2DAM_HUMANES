# HITO_2_1T_SGE_2DAM_HUMANES
HITO INDIVIDUAL SISTEMAS DE GESTIÓN EMPRESARIAL
🍷 Sistema de Encuestas de Consumo de Alcohol
👋 Sobre mí y el proyecto
Hola, soy HollyRedfield (@hollyredfield) y he desarrollado este sistema para gestionar encuestas sobre consumo de alcohol en una clínica médica.

📋 Descripción
He creado una aplicación completa con interfaz gráfica que permite gestionar y analizar encuestas sobre consumo de alcohol y sus efectos en la salud. Mi sistema utiliza Python con Tkinter para la interfaz y MySQL para el almacenamiento de datos.

✨ Características principales que he implementado
🖥️ Interfaz de Usuario
He diseñado una interfaz moderna y amigable usando Tkinter
Implementé un sistema de pestañas para organizar la información
Agregué efectos visuales y animaciones para mejorar la experiencia
📊 Gestión de Datos
Desarrollé operaciones CRUD completas para las encuestas
Añadí filtros avanzados por:
Nivel de consumo de alcohol
Edad
Sexo
Problemas de salud
Incluí ordenamiento por cualquier campo
📈 Visualización
Implementé gráficos interactivos usando matplotlib
Añadí tipos de gráficos específicos:
Consumo por edad (dispersión)
Problemas de salud (circular y barras)
Los gráficos se actualizan en tiempo real
📗 Exportación
Agregué funcionalidad para exportar a Excel
Los datos se exportan con formato adecuado
Incluí mensajes de confirmación
🛠️ Tecnologías que he utilizado
Python 3.x
Tkinter para la interfaz
MySQL para la base de datos
Pandas para manejo de datos
Matplotlib para gráficos
openpyxl para exportación Excel
📥 Instalación

1. He incluido todo lo necesario en requirements.txt:
    pip install -r requirements.txt
   
3. Necesitarás configurar la base de datos:
   
   CREATE DATABASE encuesta;
USE encuesta;
-- El script SQL completo está en database/schema.sql

🚀 Uso
Para ejecutar mi aplicación:

python main.py

📝 Configuración de la Base de Datos
He configurado la conexión en database/connection.py:

    host='localhost'
    user='root'
    password=''
    database='encuesta'

🤝 Contribuciones
Si encuentras algún problema en mi código o tienes sugerencias:

1. Abre un issue
2. Describe el problema/mejora
3. Si es posible, propón una solución

📄 Licencia
He puesto este proyecto bajo mi licencia personal (HollyRedfield).

📫 Contacto
Si necesitas contactarme:

GitHub: @hollyredfield
🙏 Agradecimientos
Agradezco la oportunidad de desarrollar esta herramienta para su clínica.

⭐ Si te gusta mi proyecto, ¡no dudes en darle una estrella!
