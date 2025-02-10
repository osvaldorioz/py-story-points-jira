from jira import JIRA
import datetime

# 📌 Configuración de Jira
JIRA_SERVER = "https://tu-dominio.atlassian.net"  # Cambia esto por tu URL de Jira
JIRA_USER = "tu-email@dominio.com"  # Tu email de Jira
JIRA_API_TOKEN = "tu-api-token"  # Tu token de API

# 📌 Conectar a Jira
options = {"server": JIRA_SERVER}
jira = JIRA(options, basic_auth=(JIRA_USER, JIRA_API_TOKEN))

# 📌 Datos del proyecto en Jira
PROJECT_KEY = "PROYECTO"  # Cambia esto por tu clave de proyecto en Jira
ISSUE_TYPE = "Story"  # Tipo de ticket (Historia de usuario)
SPRINT_ID = 123  # Opcional: ID del Sprint (si trabajas con Scrum)

def crear_historia(titulo, descripcion, prioridad="Medium", fecha_inicio=None, fecha_fin=None):
    """
    Crea una historia en Jira con fechas de inicio y fin.
    :param titulo: Título de la historia.
    :param descripcion: Descripción de la historia.
    :param prioridad: Prioridad (High, Medium, Low).
    :param fecha_inicio: Fecha de inicio (formato YYYY-MM-DD).
    :param fecha_fin: Fecha de finalización (formato YYYY-MM-DD).
    """
    issue_dict = {
        "project": {"key": PROJECT_KEY},
        "summary": titulo,
        "description": descripcion,
        "issuetype": {"name": ISSUE_TYPE},
        "priority": {"name": prioridad},
        "customfield_10015": SPRINT_ID,  # ID del Sprint (campo personalizado)
    }

    # 📌 Agregar fechas si se proporcionan
    if fecha_inicio:
        issue_dict["customfield_10010"] = fecha_inicio  # Campo personalizado para la fecha de inicio
    if fecha_fin:
        issue_dict["duedate"] = fecha_fin  # Fecha de vencimiento

    # 📌 Crear historia en Jira
    nueva_historia = jira.create_issue(fields=issue_dict)
    print(f"✅ Historia creada: {nueva_historia.key} - {titulo}")

# 📌 Ejemplo de uso
if __name__ == "__main__":
    crear_historia(
        titulo="Implementar autenticación de usuarios",
        descripcion="Desarrollar el módulo de autenticación usando JWT.",
        prioridad="High",
        fecha_inicio="2025-02-06",
        fecha_fin="2025-02-15"
    )
