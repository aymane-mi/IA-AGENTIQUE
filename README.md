# Systèmes Multi-Agents et Intelligence Artificielle Distribuée

Dépôt complet regroupant l'ensemble des travaux pratiques et laboratoires du module **Systèmes Multi-Agents et Intelligence Artificielle Distribuée** — Préparé par **Aymane MISSAOUI**.

## Structure des travaux pratiques

| Dossier | Sujet |
|---|---|
| [Lab1-prompt-engineering](./Lab1-prompt-engineering) | Ingénierie des prompts (tokenisation, Ollama, Groq, OpenAI, JSON, génération d'images) |
| [Lab2-langchain-agents](./Lab2-langchain-agents) | Agents avec LangChain (agent chef personnel, mémorisation, recherche web) |
| [Lab3-RAG](./Lab3-RAG) | Génération augmentée par récupération sur PDF (embeddings HuggingFace) + agent SQL (base Chinook) |
| [Lab4-MCP](./Lab4-MCP) | Model Context Protocol : communication stdio, serveur de temps, streaming HTTP |
| [Lab5-LangGraph_Studio](./Lab5-LangGraph_Studio) | LangGraph Studio (visualisation et débogage d'agents) + architecture multi-agents hiérarchique |
| [Lab6-Contexte_et_Etat](./Lab6-Contexte_et_Etat) | Gestion du contexte par invocation (`ReaderProfile`) et état persistant (`LibraryState`) |
| [Lab7-Human_In_The_Loop](./Lab7-Human_In_The_Loop) | Agent avec boucle humaine : interruption, approbation, rejet et édition |
| [Lab8-Workflow_avec_LangGraph](./Lab8-Workflow_avec_LangGraph) | Workflows LangGraph : graphes simples, réducteurs, état de messages, branchements conditionnels, boucles |
| [Lab9-Agent_avec_LangGraph](./Lab9-Agent_avec_LangGraph) | Agent LangGraph : outils, agent comme nœud, HITL fonctionnel (`@entrypoint`/`@task`), historique et fork |
| [TP-Chef_personnel](./TP-Chef_personnel) | Agent chef cuisinier : RAG + mémorisation + recherche web + prompt système |

## Prérequis communs

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/) — gestionnaire de paquets
- [Ollama](https://ollama.com/) avec le modèle `llama3.2:3b`

```bash
ollama pull llama3.2:3b
```

## Exécution

Chaque laboratoire est autonome avec son propre environnement virtuel :

```bash
cd Lab6-Contexte_et_Etat
uv sync
uv run --active python agent_context.py
uv run --active python agent_state.py
```

## Remarques importantes

- Les fichiers `.env` ne doivent pas être poussés sur GitHub (consulter `.env.example` dans chaque laboratoire).
- Certains laboratoires nécessitent des clés API optionnelles (`TAVILY_API_KEY`, `LANGSMITH_API_KEY`).
