from jira import JIRA
import datetime

# 📌 Configuración de Jira
JIRA_SERVER = "https://tu-dominio.atlassian.net"  # Cambia por tu URL de Jira
JIRA_USER = "tu-email@dominio.com"  # Tu email de Jira
JIRA_API_TOKEN = "tu-api-token"  # Token de API de Jira

# 📌 Conectar a Jira
options = {"server": JIRA_SERVER}
jira = JIRA(options, basic_auth=(JIRA_USER, JIRA_API_TOKEN))

# 📌 Datos del proyecto en Jira
PROJECT_KEY = "PROYECTO"  # Cambia por la clave de tu proyecto en Jira
SPRINT_ID = 123  # Opcional: ID del Sprint
VERSION_NAME = "1.0.0"  # Versión de Release

# 📌 Crear un Epic en Jira
def crear_epic(titulo, descripcion):
    issue_dict = {
        "project": {"key": PROJECT_KEY},
        "summary": titulo,
        "description": descripcion,
        "issuetype": {"name": "Epic"},
    }
    epic = jira.create_issue(fields=issue_dict)
    print(f"✅ Epic creado: {epic.key} - {titulo}")
    return epic.key  # Devuelve el ID del Epic

# 📌 Crear historias asociadas a un Epic
def crear_historia(titulo, descripcion, prioridad="Medium", epic_key=None, fecha_inicio=None, fecha_fin=None):
    issue_dict = {
        "project": {"key": PROJECT_KEY},
        "summary": titulo,
        "description": descripcion,
        "issuetype": {"name": "Story"},
        "priority": {"name": prioridad},
    }

    # 📌 Asociar la historia a un Epic (si se proporciona)
    if epic_key:
        issue_dict["customfield_10014"] = epic_key  # Epic Link (Campo personalizado)

    # 📌 Agregar fechas
    if fecha_inicio:
        issue_dict["customfield_10010"] = fecha_inicio  # Fecha de inicio
    if fecha_fin:
        issue_dict["duedate"] = fecha_fin  # Fecha de finalización

    historia = jira.create_issue(fields=issue_dict)
    print(f"✅ Historia creada: {historia.key} - {titulo}")

    return historia.key

# 📌 Crear una versión (Release)
def crear_version(version_name, descripcion, fecha_lanzamiento):
    version = jira.create_version(
        name=version_name,
        project=PROJECT_KEY,
        description=descripcion,
        releaseDate=fecha_lanzamiento,
    )
    print(f"✅ Versión creada: {version.name}")
    return version.id

# 📌 Asignar una historia a un Sprint
def asignar_a_sprint(issue_key, sprint_id):
    jira.add_issues_to_sprint(sprint_id, [issue_key])
    print(f"📌 Historia {issue_key} asignada al Sprint {sprint_id}")

# 📌 Crear un plan de trabajo
if __name__ == "__main__":
    # Crear Epic
    epic_id = crear_epic("Desarrollo de Autenticación", "Implementación del módulo de autenticación para la app")

    # Crear Historias dentro del Epic
    historia_1 = crear_historia("Diseñar API de autenticación", "Crear endpoints para login y registro", "High", epic_id, "2025-02-06", "2025-02-10")
    historia_2 = crear_historia("Implementar JWT", "Agregar autenticación con JWT y validaciones", "High", epic_id, "2025-02-11", "2025-02-15")

    # Crear una versión (Release)
    version_id = crear_version(VERSION_NAME, "Primera versión estable", "2025-03-01")

    # Asignar historias al Sprint (opcional)
    asignar_a_sprint(historia_1, SPRINT_ID)
    asignar_a_sprint(historia_2, SPRINT_ID)
