from pathlib import Path

from langchain.tools import tool

from src.config import RETRIEVAL_K
from src.vectorstore import get_vectorstore


@tool
def estimate_trip_budget(
    days: int,
    travelers: int,
    daily_budget_per_person: float,
    transport_budget: float = 0,
    activities_budget: float = 0,
) -> dict:
    """Estime le budget total d'un voyage au Maroc en MAD.

    Args:
        days: nombre de jours du sejour.
        travelers: nombre de voyageurs.
        daily_budget_per_person: budget journalier par personne en MAD
            (hebergement, repas et petits deplacements).
        transport_budget: budget transport inter-villes total en MAD.
        activities_budget: budget total des activites et excursions en MAD.
    """
    stay_budget = days * travelers * daily_budget_per_person
    total = stay_budget + transport_budget + activities_budget
    return {
        "stay_budget": round(stay_budget, 2),
        "transport_budget": round(transport_budget, 2),
        "activities_budget": round(activities_budget, 2),
        "total_budget": round(total, 2),
        "budget_per_person": round(total / travelers, 2) if travelers else 0,
    }


@tool
def suggest_itinerary(city: str, days: int, travel_style: str = "culture") -> dict:
    """Propose un mini-itineraire touristique au Maroc selon la ville, la duree
    et le style du voyage.

    Args:
        city: ville ou zone de depart (Marrakech, Fes, Tanger, Essaouira, Merzouga...).
        days: nombre de jours disponibles.
        travel_style: style dominant : culture, nature, famille, desert, plage ou budget.
    """
    city_key = city.strip().lower()
    style = travel_style.strip().lower()

    plans = {
        "marrakech": [
            "Jour 1 : medina, souks, place Jemaa el-Fna, palais Bahia",
            "Jour 2 : Jardin Majorelle, Medersa Ben Youssef, hammam ou cours de cuisine",
            "Jour 3 : excursion Atlas ou Essaouira selon le style du voyage",
        ],
        "fes": [
            "Jour 1 : medina de Fes, tanneries, ateliers d'artisanat",
            "Jour 2 : medersas, portes historiques, tombeaux merinides",
            "Jour 3 : Meknes et Volubilis ou Chefchaouen si le sejour est plus long",
        ],
        "tanger": [
            "Jour 1 : kasbah, medina, corniche",
            "Jour 2 : Cap Spartel, grottes d'Hercule, plage",
            "Jour 3 : excursion vers Assilah ou Chefchaouen",
        ],
        "essaouira": [
            "Jour 1 : medina, port, remparts, poisson",
            "Jour 2 : plage, sports de vent, balade tranquille",
            "Jour 3 : villages proches ou retour vers Marrakech",
        ],
        "merzouga": [
            "Jour 1 : arrivee, dunes, coucher de soleil",
            "Jour 2 : bivouac, balade dromadaire ou 4x4, ciel etoile",
            "Jour 3 : retour par les gorges ou vallees selon l'itineraire",
        ],
    }

    base = plans.get(city_key, [
        "Jour 1 : decouverte du centre, medina ou quartier principal",
        "Jour 2 : visite culturelle et marche locale",
        "Jour 3 : excursion proche ou activite nature",
    ])
    itinerary = base[: max(1, min(days, len(base)))]
    if days > len(base):
        itinerary.append("Jour supplementaire : ajouter une excursion proche et garder du temps libre.")

    advice = "Rythme equilibre : alterner visites, pauses et temps de transport."
    if style == "famille":
        advice = "Pour une famille : eviter les journees trop longues, prevoir pauses, eau et hebergement central."
    elif style == "budget":
        advice = "Pour petit budget : privilegier bus/train, restaurants locaux et visites gratuites."
    elif style == "desert":
        advice = "Pour le desert : prevoir vetements chauds la nuit et reserver le bivouac avec un prestataire fiable."
    elif style == "plage":
        advice = "Pour la plage : verifier la saison, le vent et choisir un logement proche du front de mer."

    return {"city": city, "days": days, "style": travel_style, "itinerary": itinerary, "advice": advice}


@tool
def retrieve_documents(query: str) -> str:
    """Recherche dans la base documentaire de tourisme au Maroc
    (destinations, transport, hebergement, activites, conseils de voyage) les
    passages les plus pertinents pour une question.

    Args:
        query: la question ou les mots-cles a rechercher.
    """
    vectorstore = get_vectorstore()
    docs = vectorstore.similarity_search(query, k=RETRIEVAL_K)
    if not docs:
        return "Aucun document pertinent trouve."
    formatted = []
    for doc in docs:
        source = Path(doc.metadata.get("source", "inconnu")).name
        page = doc.metadata.get("page", "?")
        formatted.append(f"[Source: {source}, page {page}]\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


TOOLS = [retrieve_documents, estimate_trip_budget, suggest_itinerary]
TOOLS_BY_NAME = {t.name: t for t in TOOLS}
