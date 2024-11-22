import nox  # type: ignore


# Instalar dependencias desde requirements.txt 
@nox.session
def install_from_requirements(session):
    """
    Instala las dependencias definidas en requirements.txt.
    Este es el único lugar donde se instalan las dependencias para evitar duplicación en las sesiones.
    """
    # Ejecutar el comando pip para instalar las dependencias desde el archivo requirements.txt
    session.run("pip", "install", "-r", "requirements.txt")


# Ejecutar todas las pruebas y generar un reporte HTML
@nox.session(reuse_venv=True)
def run_tests(session):
    """
    Ejecuta las pruebas con pytest y genera un reporte HTML.
    Esta sesión reutiliza el entorno virtual de la sesión 'install_from_requirements'.
    """
    # Verifica si las dependencias ya están instaladas
    # Ejecutar las pruebas con pytest y generar el reporte HTML
    session.run("pytest", "--html=report.html")


@nox.session(reuse_venv=True)
def lint_and_format(session):
    """
    Realiza el formateo y linting del código con black.
    Asegura que 'black' esté instalado en el entorno y formatea el código.
    """
    # Instalar black si no está instalado
    session.install(
        "black"
    )  # Instala black para formatear el código si no está presente
    # Ejecutar black en el directorio actual para formatear el código
    session.run("black", ".")


# Probar distintas versiones de Python
@nox.session(python=["3.8", "3.9", "3.10"], reuse_venv=True)
def tests_on_versions(session):
    """
    Ejecuta pruebas en diferentes versiones de Python.
    Esta sesión reutiliza el entorno virtual y ejecuta pruebas en varias versiones de Python.
    """
    
    # Ejecutar las pruebas en esta versión de Python
    session.run("pytest")


