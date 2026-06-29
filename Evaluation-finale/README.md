# Assistant Touristique Intelligent - Agentic RAG avec LangGraph

Projet d'evaluation finale : systeme **Agentic RAG** construit avec **LangGraph**
(sans `create_agent`) sur le domaine du **tourisme au Maroc**.

L'assistant repond a des questions sur les destinations, les itineraires, le
transport, l'hebergement, les activites, les saisons, le budget et les conseils
de voyage.

## Stack

- LLM : Ollama local `llama3.2:3b`
- Embeddings : `sentence-transformers/all-MiniLM-L6-v2`
- Vectorstore : Chroma persiste dans `data/chroma_db/`
- Orchestration : LangGraph `StateGraph`

## Installation

```bash
uv sync --group dev
ollama pull llama3.2:3b
```

## Base documentaire

Les PDF touristiques sont dans `data/pdfs/` :

- destinations et saisons au Maroc ;
- transport et hebergement ;
- activites et conseils de voyage.

Construire le vectorstore :

```bash
uv run python ingest.py
```

## Utilisation

```bash
uv run python main.py
```

Exemples de questions :

```text
Quel itineraire pour 3 jours a Marrakech ?
Combien coute un voyage de 5 jours pour 2 personnes avec 400 MAD par jour ?
Quelle est la meilleure periode pour visiter le desert ?
Comment aller de Marrakech vers Merzouga ?
```

## Architecture du graphe

Le graphe suit un workflow Agentic RAG :

1. `agent` : decide de repondre ou d'appeler un outil ;
2. `tools` : execute `retrieve_documents`, `suggest_itinerary` ou `estimate_trip_budget` ;
3. `grade_documents` : verifie la pertinence des documents recuperes ;
4. `rewrite_query` : reformule la requete si les documents ne sont pas pertinents ;
5. retour vers `agent` pour produire la reponse finale.

Generation du graphe :

```bash
uv run python generate_graph.py
```

## Outils

- `retrieve_documents(query)` : recherche semantique dans les PDF touristiques.
- `suggest_itinerary(city, days, travel_style)` : propose un itineraire selon la ville et le style.
- `estimate_trip_budget(days, travelers, daily_budget_per_person, transport_budget, activities_budget)` : calcule un budget total en MAD.

## Evaluation

```bash
uv run python -m evaluation.run_evaluation
```

Le script execute 10 questions simples + 10 questions complexes, mesure le temps
de reponse et sauvegarde les resultats dans `evaluation/results/results.csv`.

## Tests

```bash
uv run pytest -v
```
