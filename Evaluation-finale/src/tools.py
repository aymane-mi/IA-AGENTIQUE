from pathlib import Path

from langchain.tools import tool

from src.config import RETRIEVAL_K


def _load_vectorstore():
    """Import paresseux pour eviter de charger Chroma/HuggingFace pendant les tests unitaires."""
    from src.vectorstore import get_vectorstore

    return get_vectorstore()


@tool
def estimate_trip_budget(
    number_of_days: int,
    number_of_people: int,
    accommodation_per_night: float,
    food_per_person_per_day: float,
    transport_total: float,
    activities_per_person: float = 0,
) -> dict:
    """Estime le budget total d'un voyage touristique en dirhams marocains (MAD)."""
    if number_of_days <= 0 or number_of_people <= 0:
        raise ValueError("Le nombre de jours et de voyageurs doit etre positif.")
    nights = max(number_of_days - 1, 0)
    accommodation = nights * accommodation_per_night
    food = number_of_days * number_of_people * food_per_person_per_day
    activities = number_of_people * activities_per_person
    total = accommodation + food + transport_total + activities
    return {
        "nights": nights,
        "accommodation": round(accommodation, 2),
        "food": round(food, 2),
        "transport": round(transport_total, 2),
        "activities": round(activities, 2),
        "total_budget": round(total, 2),
        "budget_per_person": round(total / number_of_people, 2),
    }


@tool
def suggest_destination_by_season(season: str, travel_style: str = "culture") -> dict:
    """Propose une destination marocaine selon la saison et le style de voyage."""
    s = season.strip().lower()
    style = travel_style.strip().lower()
    table = {
        "printemps": {
            "culture": "Fes ou Marrakech",
            "nature": "Vallee des Roses et Atlas",
            "desert": "Merzouga avant les fortes chaleurs",
            "plage": "Essaouira ou Agadir",
            "budget": "Chefchaouen et Tetouan",
            "famille": "Marrakech avec excursions courtes",
        },
        "ete": {
            "culture": "Rabat ou Tanger avec visites en matinee",
            "nature": "Ifrane, Azrou et Moyen Atlas",
            "desert": "A eviter en pleine journee; preferer l'automne",
            "plage": "Essaouira, Agadir ou Saidia",
            "budget": "Asilah et villes du nord hors pics touristiques",
            "famille": "Agadir ou Essaouira",
        },
        "automne": {
            "culture": "Fes, Meknes et Volubilis",
            "nature": "Atlas et oasis du Sud",
            "desert": "Merzouga ou Zagora",
            "plage": "Agadir et Essaouira",
            "budget": "Marrakech hors haute saison",
            "famille": "Circuit Marrakech - Ouarzazate",
        },
        "hiver": {
            "culture": "Marrakech, Fes ou Rabat",
            "nature": "Oukaimeden, Ifrane et Atlas",
            "desert": "Merzouga ou Zagora avec nuits froides",
            "plage": "Agadir pour climat doux",
            "budget": "Rabat, Meknes ou Fes",
            "famille": "Agadir ou Marrakech",
        },
    }
    choices = table.get(s, table["printemps"])
    destination = choices.get(style, choices["culture"])
    return {
        "season": season,
        "travel_style": travel_style,
        "recommended_destination": destination,
        "advice": "Verifiez toujours les horaires, la meteo et les conditions locales avant le depart.",
    }


@tool
def retrieve_documents(query: str) -> str:
    """Recherche dans la base documentaire touristique les passages les plus pertinents."""
    vectorstore = _load_vectorstore()
    docs = vectorstore.similarity_search(query, k=RETRIEVAL_K)
    if not docs:
        return "Aucun document pertinent trouve."
    formatted = []
    for doc in docs:
        source = Path(doc.metadata.get("source", "inconnu")).name
        page = doc.metadata.get("page", "?")
        formatted.append(f"[Source: {source}, page {page}]\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


TOOLS = [retrieve_documents, estimate_trip_budget, suggest_destination_by_season]
TOOLS_BY_NAME = {t.name: t for t in TOOLS}
