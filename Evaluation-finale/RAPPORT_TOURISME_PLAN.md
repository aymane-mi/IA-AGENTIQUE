# Rapport individuel - Assistant Touristique Agentic RAG

## 1. Demarche suivie
Le projet implemente un assistant touristique intelligent base sur l'approche Agentic RAG. La base documentaire contient des PDF sur les destinations marocaines, le transport, l'hebergement, les activites et les conseils de voyage.

## 2. Fonctionnement du systeme
Le systeme utilise LangGraph avec les noeuds agent, tools, grade_documents et rewrite_query. L'agent choisit entre la recherche documentaire, la suggestion d'itineraire, l'estimation de budget ou une reponse finale.

## 3. Evaluation
L'evaluation contient 10 questions simples et 10 questions complexes. Les resultats sont sauvegardes dans evaluation/results/results.csv avec le temps de reponse, les sources recuperees et le nombre d'appels LLM.

## 4. Limites et ameliorations
Les limites principales sont la taille reduite de la base documentaire, la dependance au modele local Ollama et l'absence de donnees temps reel. Les ameliorations possibles incluent l'ajout de donnees officielles, une API meteo et une interface web.
