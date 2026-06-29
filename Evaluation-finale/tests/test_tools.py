import pytest

from src.tools import estimate_trip_budget, suggest_itinerary


def test_estimate_trip_budget():
    result = estimate_trip_budget.invoke({
        "days": 5,
        "travelers": 2,
        "daily_budget_per_person": 400,
        "transport_budget": 1200,
        "activities_budget": 800,
    })
    assert result["stay_budget"] == pytest.approx(4000.00, abs=0.01)
    assert result["total_budget"] == pytest.approx(6000.00, abs=0.01)
    assert result["budget_per_person"] == pytest.approx(3000.00, abs=0.01)


def test_suggest_itinerary_marrakech():
    result = suggest_itinerary.invoke({"city": "Marrakech", "days": 2, "travel_style": "culture"})
    assert result["city"] == "Marrakech"
    assert len(result["itinerary"]) == 2
    assert "medina" in result["itinerary"][0].lower()
