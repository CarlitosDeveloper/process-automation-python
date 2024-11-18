@echo off
setlocal EnableDelayedExpansion

:menu
cls
echo ================================
echo Python Virtual Environment Manager
echo ================================
echo 0. Salir
echo 1. Crear un entorno virtual (myenv)
echo 2. Activar el entorno virtual
echo 3. Instalar dependencias desde requirements.txt
echo 4. Listar dependencias actuales
echo 5. Guardar dependencias actuales en requirements.txt
echo 6. Desactivar el entorno virtual
echo 7. Eliminar el entorno virtual
echo 8. Ejecutar Create_Executables.py
echo 9. Ejecutar Draw_Folder_Layout.py
echo ================================
set /p opcion="Ingrese el número del comando: "

if "%opcion%"=="0" (
    echo Saliendo...
    exit /b
) else if "%opcion%"=="1" (
    python -m venv myenv
    pause
) else if "%opcion%"=="2" (
    echo Activando el entorno virtual...
    call myenv\Scripts\activate
    if errorlevel 1 (
        echo No se pudo activar el entorno virtual. Verifica si "myenv" existe.
    ) else (
        echo Entorno virtual activado.
        echo Escribe "deactivate" para salir.
        cmd /k
    )
) else if "%opcion%"=="3" (
    call myenv\Scripts\activate && pip install -r requirements.txt && deactivate
    pause
) else if "%opcion%"=="4" (
    call myenv\Scripts\activate && pip list && deactivate
    pause
) else if "%opcion%"=="5" (
    call myenv\Scripts\activate && pip freeze > requirements.txt && deactivate
    pause
) else if "%opcion%"=="6" (
    deactivate
    pause
) else if "%opcion%"=="7" (
    rd /s /q myenv
    echo Entorno virtual eliminado.
    pause
) else if "%opcion%"=="8" (
    python Create_Executables.py
    pause
) else if "%opcion%"=="9" (
    python Draw_Folder_Layout.py
    pause
) else (
    echo Comando no reconocido, por favor intente nuevamente.
    pause
    goto menu
)

goto menu
