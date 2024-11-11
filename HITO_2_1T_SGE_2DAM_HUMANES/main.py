# En este archivo principal, he creado el punto de entrada de mi aplicación.
# Empiezo importando los módulos necesarios para mi interfaz gráfica
import os
import sys
# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tkinter as tk
from views.main_window import MainWindow

# Aquí defino mi función principal que inicia la aplicación.
def main():
    # Creo la ventana raíz que contendrá toda mi aplicación
    # Creo la ventana raíz de tkinter
    root = tk.Tk()
    try:
        # Intento aplicar un tema visual moderno usando sv_ttk
        # Si está disponible, lo configuro en modo claro
        import sv_ttk
        sv_ttk.set_theme("light")
    except ImportError:
        # Si no encuentro sv_ttk, informo que usaré el tema básico
        print("[INFO] Ejecutando con tema visual básico")
    
    # Creo mi ventana principal personalizada
    app = MainWindow(root)
    # Inicio el bucle principal de eventos de la interfaz
    root.mainloop()

# He añadido este bloque de control para cuando ejecuto el archivo directamente
if __name__ == "__main__":
    try:
        # Intento importar y ejecutar la configuración inicial
        import setup
        if setup.setup():
            # Si la configuración es exitosa, inicio la aplicación
            main()
        else:
            # Si hay error en la configuración, lo informo
            print("[ERROR] Error en la configuración inicial")
    except ImportError as e:
        # Si no encuentro el módulo setup, informo y ejecuto la app de todas formas
        print(f"[ADVERTENCIA] Ejecutando sin verificación de dependencias: {e}")
        main()