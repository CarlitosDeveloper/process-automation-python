@echo off
:menu
cls
echo ================================
echo Seleccione el comando que desea ejecutar:
echo ================================
echo 00. Salir
echo 01. Delete repeat in all sub folders - Picture
echo 02. Detect repeat in all sub folders - Picture (Percentage)
echo 03. Change format in all sub folders - Picture (JPG)
echo 04. Change format in all sub folders - Picture (JPEG)
echo 05. Delete repeat in all sub folders - Video
echo 06. Change format in all sub folders - Video
echo 07. Detect (Folders, Sub folders, Files).
echo 08. Detect (Folders, Sub folders).
echo 09. Charge All files (.py) in (.exe)
echo 10. Carpeta1 vs Carpeta2

echo ================================
set /p opcion="Ingrese el número del comando:"

if "%opcion%"=="0" (
    echo Saliendo...
    exit /b
) else if "%opcion%"=="1" (
    python src\apps\Delete_Repeat_Picture.py
) else if "%opcion%"=="2" (
    python src\apps\Detect_Repeat_Images_By_Percentage.py
) else if "%opcion%"=="3" (
    python src\apps\Change_Format_Picture_JPG.py
) else if "%opcion%"=="4" (
    python src\apps\Change_Format_Picture_JPEG.py
) else if "%opcion%"=="5" (
    python src\apps\Delete_Repeat_Video.py
) else if "%opcion%"=="6" (
    python src\apps\Change_Format_Video.py
) else if "%opcion%"=="7" (
    python src\apps\Draw_Folder_Layout_Files.py
) else if "%opcion%"=="8" (
    python src\apps\Draw_Folder_Layout.py
) else if "%opcion%"=="9" (
    python Create_Executables.py
) else if "%opcion%"=="10" (
    python src\apps\Carpeta1VsCarpeta2.py
) else (
    echo Comando no reconocido, por favor intente nuevamente.
    pause
    goto menu
)
