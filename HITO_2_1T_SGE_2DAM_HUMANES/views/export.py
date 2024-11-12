import pandas as pd
from tkinter import messagebox, ttk

def export_to_excel(tree: ttk.Treeview, file_path: str):
    """
    Exporta los datos del TreeView a un archivo Excel
    
    Args:
        tree: El TreeView que contiene los datos
        file_path: La ruta donde guardar el archivo Excel
    """
    try:
        data = []
        columns = tree["columns"]
        
        for item in tree.get_children():
            values = tree.item(item)["values"]
            row = dict(zip(columns, values))
            data.append(row)
        
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
        
        messagebox.showinfo("Éxito", "Datos exportados correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar: {str(e)}")
