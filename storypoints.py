import requests
import json

# Configuración de Jira
JIRA_URL = "https://tu-jira.atlassian.net"
JQL_QUERY = "project=MI_PROYECTO AND issuetype=Story AND Sprint in openSprints() AND resolution IS NOT EMPTY AND 'Story Points' IS NOT EMPTY"
AUTH = ("tu_email", "tu_token")  # Usa tu API token

def obtener_issues():
    url = f"{JIRA_URL}/rest/api/2/search"
    params = {"jql": JQL_QUERY, "maxResults": 100, "fields": ["Sprint", "customfield_10002"]}  # customfield_10002 = Story Points
    response = requests.get(url, auth=AUTH, params=params)
    return response.json()["issues"]

def calcular_promedio_story_points(issues):
    sprint_story_points = {}
    
    for issue in issues:
        story_points = issue["fields"].get("customfield_10002", 0)
        sprints = issue["fields"].get("Sprint", [])

        for sprint in sprints:
            sprint_name = sprint["name"]
            if sprint_name not in sprint_story_points:
                sprint_story_points[sprint_name] = []
            sprint_story_points[sprint_name].append(story_points)

    # Calcular promedio por sprint
    promedios = {sprint: sum(points) / len(points) for sprint, points in sprint_story_points.items()}
    return promedios

issues = obtener_issues()
promedios = calcular_promedio_story_points(issues)

for sprint, avg in promedios.items():
    print(f"Sprint: {sprint} - Promedio Story Points: {avg:.2f}")
