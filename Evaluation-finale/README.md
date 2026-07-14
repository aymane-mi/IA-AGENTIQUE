# Evaluation finale - Agentic RAG (Assistant Touristique Intelligent)

Systeme RAG agentique construit avec LangGraph (sans `create_agent`), sur le
theme du tourisme au Maroc : destinations, circuits, saisons, transport, budget,
culture et conseils pratiques.

## Stack

- LLM : Ollama local `llama3.2:3b`
- Embeddings : HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
- Vectorstore : Chroma (persiste dans `data/chroma_db/`)
- Orchestration : LangGraph (`StateGraph`)

## Installation

```bash
uv sync --group dev
```

Assurez-vous qu'Ollama est lance et que le modele est disponible :

```bash
ollama pull llama3.2:3b
```

## Base documentaire

La base documentaire contient plusieurs PDF synthetiques sur le tourisme au Maroc :
Marrakech/Atlas/Essaouira, Fes/Rabat/Chefchaouen, desert marocain et conseils
pratiques de voyage.

```bash
uv run python download_pdfs.py   # cree les PDF touristiques dans data/pdfs/
uv run python ingest.py          # construit le vectorstore Chroma
```

## Utilisation

```bash
uv run python main.py
```

Chat interactif avec memoire conversationnelle (un `thread_id` par session).

## Architecture du graphe

```bash
uv run python generate_graph.py
```

Le graphe suit le pattern Agentic RAG :

- `agent` : le LLM decide d'appeler `retrieve_documents`, `estimate_trip_budget`,
  `suggest_destination_by_season`, ou de repondre directement.
- `tools` : execute les outils demandes.
- `grade_documents` : evalue la pertinence des documents recuperes.
- `rewrite_query` : reformule la question si les documents ne sont pas pertinents
  (jusqu'a 2 fois), puis retourne a `agent`.

La memoire conversationnelle est assuree par un `InMemorySaver` (checkpointer)
indexe par `thread_id`.

## Outils

- `retrieve_documents(query)` : recherche semantique dans la base documentaire touristique.
- `estimate_trip_budget(...)` : estimation d'un budget de voyage en MAD.
- `suggest_destination_by_season(season, travel_style)` : recommandation de destination
  selon la saison et le style de voyage.

## Tests

```bash
uv run pytest -v
```

## Evaluation

```bash
uv run python -m evaluation.run_evaluation
```

Execute 10 questions simples + 10 questions complexes, mesure le temps de
reponse et enregistre les sources recuperees dans `evaluation/results/results.csv`.
