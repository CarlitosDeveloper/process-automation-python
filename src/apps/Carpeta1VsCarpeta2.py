import os
from PIL import Image
from hashlib import md5

def calcular_hash_imagen(ruta_imagen):
    """Calcula el hash de una imagen usando su contenido en bytes."""
    try:
        with Image.open(ruta_imagen) as img:
            return md5(img.tobytes()).hexdigest()
    except Exception:
        return None

def obtener_hashes_carpeta(ruta_carpeta):
    """Obtiene un diccionario de hashes para todas las imágenes de una carpeta."""
    hashes = {}
    for root, dirs, files in os.walk(ruta_carpeta):
        for archivo in files:
            ruta_archivo = os.path.join(root, archivo)
            hash_imagen = calcular_hash_imagen(ruta_archivo)
            if hash_imagen:
                hashes[hash_imagen] = ruta_archivo
    return hashes

def eliminar_duplicados(carpeta1, carpeta2):
    """Compara imágenes entre dos carpetas y elimina duplicados en la carpeta 2."""
    hashes_carpeta1 = obtener_hashes_carpeta(carpeta1)
    hashes_carpeta2 = obtener_hashes_carpeta(carpeta2)

    duplicados_encontrados = []

    for hash_imagen, ruta_imagen2 in hashes_carpeta2.items():
        if hash_imagen in hashes_carpeta1:
            duplicados_encontrados.append((ruta_imagen2, hashes_carpeta1[hash_imagen]))
            os.remove(ruta_imagen2)  # Elimina la imagen duplicada de carpeta 2

    return duplicados_encontrados

if __name__ == "__main__":
    carpeta1 = input("Introduce la ruta de la carpeta 1: ")
    carpeta2 = input("Introduce la ruta de la carpeta 2: ")

    duplicados = eliminar_duplicados(carpeta1, carpeta2)

    if duplicados:
        print("Imágenes duplicadas eliminadas:")
        for img2, img1 in duplicados:
            print(f"  - {img2} es un duplicado de {img1} y ha sido eliminado.")
    else:
        print("No se encontraron imágenes duplicadas entre las carpetas.")
