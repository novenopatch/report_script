import os
import git
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from jinja2 import Template
import plotly.express as px

repo = git.Repo(".")
branch = repo.active_branch.name

commits = list(repo.iter_commits(branch))
total_commits = len(commits)

authors = [commit.author.name for commit in commits]
author_counter = Counter(authors)

file_changes = Counter()
for commit in commits:
    author = commit.author.name
    try:
        files = commit.stats.files
        file_changes[author] += len(files)
    except:
        continue

data = pd.DataFrame({
    "Auteur": list(author_counter.keys()),
    "Commits": list(author_counter.values()),
    "Fichiers modifiés": [file_changes[author] for author in author_counter.keys()],
})

plt.figure(figsize=(10, 6))
data.sort_values("Commits", ascending=False).plot.barh(
    x="Auteur", y="Commits", color="skyblue", legend=False
)
plt.title("Nombre de commits par contributeur")
plt.tight_layout()
plt.savefig("commits_per_author.png")

plt.figure(figsize=(10, 6))
data.sort_values("Fichiers modifiés", ascending=False).plot.barh(
    x="Auteur", y="Fichiers modifiés", color="orange", legend=False
)
plt.title("Nombre de fichiers modifiés par contributeur")
plt.tight_layout()
plt.savefig("files_per_author.png")

fig = px.bar(
    data,
    x="Auteur",
    y="Commits",
    color="Fichiers modifiés",
    title="Contributions Git",
    labels={"Commits": "Nombre de commits", "Auteur": "Contributeurs"},
    text="Commits",
)
fig.write_html("commits_interactive.html")

template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport de contributions Git</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-4">
    <h1 class="mb-4">Rapport de contributions Git</h1>
    <p><strong>Branche analysée :</strong> {{ branch }}</p>
    <p><strong>Total de commits :</strong> {{ total_commits }}</p>

    <h2>Graphiques</h2>
    <div class="row">
        <div class="col-md-6">
            <h4>Nombre de commits par contributeur</h4>
            <img src="commits_per_author.png" alt="Commits par contributeur" class="img-fluid">
        </div>
        <div class="col-md-6">
            <h4>Nombre de fichiers modifiés par contributeur</h4>
            <img src="files_per_author.png" alt="Fichiers modifiés par contributeur" class="img-fluid">
        </div>
    </div>

    <h2>Détails</h2>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Auteur</th>
                <th>Nombre de commits</th>
                <th>Nombre de fichiers modifiés</th>
            </tr>
        </thead>
        <tbody>
        {% for index, row in data.iterrows() %}
            <tr>
                <td>{{ row['Auteur'] }}</td>
                <td>{{ row['Commits'] }}</td>
                <td>{{ row['Fichiers modifiés'] }}</td>
            </tr>
        {% endfor %}
        </tbody>
    </table>

    <h2>Graphique interactif</h2>
    <iframe src="commits_interactive.html" width="100%" height="600"></iframe>
</div>
</body>
</html>
""")

html_content = template.render(branch=branch, total_commits=total_commits, data=data)

with open("rapport_contributions.html", "w") as f:
    f.write(html_content)

print("Rapport généré : rapport_contributions.html")
