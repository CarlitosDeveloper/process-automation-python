@echo off
echo Seleccione el comando que desea ejecutar:
echo 1. Delete repeated images in all subfolders
echo 2. Change format of images in all subfolders (GIF, JPEG)
echo 3. Rename all files based on their folders
echo 4. Rename all files using counter

set /p opcion="Ingrese el numero del comando: "
if "%opcion%"=="1" (
    python src\delete-repeat-all-subfolders.py
) else if "%opcion%"=="2" (
    python src\change-format-all-subfolders.PY
) else if "%opcion%"=="3" (
    python src\change-name-all-subfolders.py
) else if "%opcion%"=="4" (
    python src\change-name-all-subfolders-using-counter.py
) else (
    echo Comando no reconocido
)
