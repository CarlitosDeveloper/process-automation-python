import os
import subprocess

# Ruta relativa a la carpeta principal del proyecto
ruta_carpeta = os.path.join('src', 'apps')
ruta_salida = os.path.join('executables')
ruta_log = os.path.join('temp', 'conversion_log.txt')

# Crear carpeta de salida y de log si no existen
os.makedirs(ruta_salida, exist_ok=True)
os.makedirs(os.path.dirname(ruta_log), exist_ok=True)

for archivo in os.listdir(ruta_carpeta):
    if archivo.endswith('.py'):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        nombre_ejecutable = os.path.splitext(archivo)[0] + '.exe'
        ruta_ejecutable = os.path.join(ruta_salida, nombre_ejecutable)
        
        # Evitar recompilación si el ejecutable ya existe
        if os.path.exists(ruta_ejecutable):
            print(f"Ejecutable {nombre_ejecutable} ya existe. Saltando...")
            continue

        try:
            # Ejecutar PyInstaller con el directorio de salida especificado
            subprocess.run(
                ['pyinstaller', '--onefile', '--windowed', '--distpath', ruta_salida, ruta_archivo],
                check=True
            )
            print(f"Ejecutable {nombre_ejecutable} creado exitosamente.")
        except subprocess.CalledProcessError as e:
            # Registrar cualquier error en el archivo de log
            with open(ruta_log, 'a') as log_file:
                log_file.write(f"Error al convertir {archivo}: {e}\n")
            print(f"Error al convertir {archivo}. Consultar el log para más detalles.")
