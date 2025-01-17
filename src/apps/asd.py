import os

def rename_files_by_folder(base_folder_path):
    # Verifica si la ruta existe
    if not os.path.exists(base_folder_path):
        print(f"La ruta {base_folder_path} no existe.")
        return

    # Recorre la carpeta y sus subcarpetas
    for main_path, sub_folders, files in os.walk(base_folder_path):
        # Obtiene el nombre de la carpeta actual
        folder_name = os.path.basename(main_path)
        
        # Inicializa el contador para los archivos de esta carpeta
        counter = 0

        for file_name in files:
            # Obtiene la extensión del archivo preservando su formato original
            _, file_extension = os.path.splitext(file_name)

            # Construye el nuevo nombre del archivo en el formato solicitado
            new_file_name = f"{folder_name.upper()}_{file_extension[1:].upper()} ({counter}).{file_extension[1:]}"
            
            # Construye las rutas completas
            old_file_path = os.path.join(main_path, file_name)
            new_file_path = os.path.join(main_path, new_file_name)

            try:
                # Renombra el archivo
                os.rename(old_file_path, new_file_path)
                print(f"Renombrado: {old_file_path} -> {new_file_path}")
                
                # Incrementa el contador
                counter += 1
            except Exception as e:
                print(f"Error al renombrar el archivo {file_name}: {e}")

if __name__ == "__main__":
    # Solicita al usuario la ruta de la carpeta base
    base_folder_path = input("Ingresa la ruta de la carpeta base: ")
    rename_files_by_folder(base_folder_path)
