import nox  # type: ignore


# Instalar dependencias desde requirements.txt
@nox.session
def install_from_requirements(session):
    """
    Instala las dependencias definidas en requirements.txt.
    """
    session.run(
        "pip", "install", "-r", "requirements.txt"
    )  


# Sesión principal para ejecutar pruebas
@nox.session
def run_tests(session):
    """
    Ejecuta las pruebas con pytest.
    """
    session.run(
        "pytest"
    )  


@nox.session
def lint_and_format(session):
    """
    Realiza el formateo y linting del código con black
    """
    session.run("black", ".")


# Pruebas con pytest-asyncio
@nox.session
def async_tests(session):
    """
    Ejecuta pruebas asíncronas con pytest-asyncio.
    """
    session.run(
        "pytest"
    )  


# Probar distintas versiones de Python
@nox.session(python=["3.8", "3.9", "3.10"])
def tests_on_versions(session):
    """
    Ejecuta pruebas en diferentes versiones de Python.
    """
    session.run(
        "pytest"
    )  


# Actualizar requirements.txt utilizando pip-tools
@nox.session
def update_requirements(session):
    """
    Actualiza el archivo requirements.txt utilizando pip-tools.
    """
    session.install("pip-tools")  
    session.run("pip-compile", "--output-file=requirements.txt")


# Ejecutar pruebas con reporte HTML
@nox.session
def html_report_tests(session):
    """
    Ejecuta pruebas y genera un reporte HTML.
    """
    session.run("pytest", "--html=report.html")
