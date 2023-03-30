# Spécifie l'image de base
FROM python:3

# Crée un répertoire de travail
WORKDIR /app

# Copie les fichiers requis dans le conteneur
COPY requirements.txt ./
COPY script.py ./

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exécute le script Python
CMD [ "python", "./script.py" ]