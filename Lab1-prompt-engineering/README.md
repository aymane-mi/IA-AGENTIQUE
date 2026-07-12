# TP 1 : Ingénierie des prompts

Travail pratique couvrant les fondamentaux de l'ingénierie des prompts, de la tokenisation à la génération d'images avec différents fournisseurs de modèles.

## Contenu des exercices

- `01_tokenisation.py` : Tokenisation et comptage de tokens avec `tiktoken`
- `02_ollama_prompt.py` : Invocation simple de prompts avec Ollama
- `03_groq_prompt.py` : Invocation simple de prompts avec Groq
- `04_openai_prompt.py` : Invocation simple de prompts avec OpenAI
- `05_aspect_sentiment_json.py` : Analyse de sentiment avec sortie structurée en JSON
- `06_image_generation.py` : Génération d'images via API
- `07_image_description.py` : Description et analyse de l'image `rag.png`

## Installation et configuration de l'environnement

Créer et initialiser l'environnement virtuel avec `uv` :

```bash
uv venv
uv sync
```

### Activation de l'environnement

Sous Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Sous bash/Linux/macOS :

```bash
source .venv/bin/activate
```

## Configuration des clés API

Copier le fichier `.env.example` vers `.env` et renseigner les variables :

```env
OPENAI_API_KEY=...
GROQ_API_KEY=...
OLLAMA_MODEL=llama3.2:3b
```

## Exécution des scripts

Chaque script s'exécute indépendamment :

```bash
python 01_tokenisation.py
python 02_ollama_prompt.py
python 03_groq_prompt.py
python 04_openai_prompt.py
python 05_aspect_sentiment_json.py
python 06_image_generation.py
python 07_image_description.py
```

## Remarques importantes

- `01_tokenisation.py` fonctionne sans clé API.
- `02_ollama_prompt.py` nécessite un serveur Ollama actif et un modèle local installé.
- Les scripts `03` à `07` requièrent des clés API valides pour les services respectifs.
