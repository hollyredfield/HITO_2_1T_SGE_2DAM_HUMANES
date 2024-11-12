# Este es mi módulo de configuración inicial que verifica y prepara el entorno

# Primero importo las bibliotecas que necesito:
# - subprocess: para ejecutar comandos pip
# - sys: para acceder al ejecutable de Python
# - importlib: para verificar si los módulos están instalados
# - platform: para información del sistema
import subprocess
import sys
import importlib
import platform

# Esta función verifica si un paquete está instalado y lo instala si es necesario
def check_and_install_package(package_name):
    try:
        # Intento importar el paquete para ver si ya está instalado
        # Limpio el nombre del paquete por si tiene caracteres especiales
        module_name = package_name.replace('-', '_').split('>=')[0]
        importlib.import_module(module_name)
        print(f"[OK] {package_name} ya esta instalado")
    except ImportError:
        # Si no está instalado, procedo a instalarlo con pip
        print(f"[+] Instalando {package_name}...")
        try:
            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                package_name
            ])
            print(f"[OK] {package_name} instalado correctamente")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] No se pudo instalar {package_name}: {e}")
            return False
    return True

# Mi función principal de configuración
def setup():
    print("Verificando e instalando dependencias necesarias...")
    
    # Defino la lista de paquetes que necesito con sus versiones mínimas
    required_packages = [
        'mysql-connector-python>=8.0.0',
        'openpyxl>=3.0.0',
        'pandas>=1.0.0',
        'matplotlib>=3.0.0',
        'pillow>=8.0.0'
    ]

    # Intento instalar cada paquete y guardo los que fallan
    failed_packages = []
    for package in required_packages:
        if not check_and_install_package(package):
            failed_packages.append(package)

    # Informo sobre el resultado de las instalaciones
    if failed_packages:
        print("\n[ADVERTENCIA] Los siguientes paquetes no se pudieron instalar:")
        for package in failed_packages:
            print(f"  - {package}")
        print("La aplicación podría no funcionar correctamente.")
    else:
        print("\n[OK] Todas las dependencias están instaladas correctamente.")

    return len(failed_packages) == 0

# Esta función prueba si puedo conectarme a la base de datos
def test_database():
    """Prueba la conexión a la base de datos"""
    try:
        from database.connection import DBConnection
        db = DBConnection()
        db.connect()
        print("[OK] Conexión a la base de datos exitosa")
        return True
    except Exception as e:
        print(f"[ERROR] Error en la conexión a la base de datos: {e}")
        return False

# Bloque de ejecución principal
if __name__ == "__main__":
    # Si ejecuto este archivo directamente:
    # 1. Verifico la instalación de dependencias
    # 2. Pruebo la conexión a la base de datos
    # 3. Si todo está bien, inicio la aplicación
    if setup():
        if test_database():
            print("[OK] Sistema listo para ejecutar")
            import main
            main.main()
        else:
            print("[ERROR] No se pudo conectar a la base de datos")
    else:
        print("[ERROR] La configuración no se completó correctamente")