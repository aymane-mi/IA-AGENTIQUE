import pytest

from src.tools import estimate_trip_budget, suggest_destination_by_season


def test_estimate_trip_budget():
    result = estimate_trip_budget.invoke({
        "number_of_days": 4,
        "number_of_people": 2,
        "accommodation_per_night": 450,
        "food_per_person_per_day": 120,
        "transport_total": 700,
        "activities_per_person": 300,
    })
    assert result["nights"] == 3
    assert result["accommodation"] == pytest.approx(1350.00, abs=0.01)
    assert result["food"] == pytest.approx(960.00, abs=0.01)
    assert result["activities"] == pytest.approx(600.00, abs=0.01)
    assert result["total_budget"] == pytest.approx(3610.00, abs=0.01)
    assert result["budget_per_person"] == pytest.approx(1805.00, abs=0.01)


def test_estimate_trip_budget_invalid_values():
    with pytest.raises(ValueError):
        estimate_trip_budget.invoke({
            "number_of_days": 0,
            "number_of_people": 2,
            "accommodation_per_night": 450,
            "food_per_person_per_day": 120,
            "transport_total": 700,
        })


def test_suggest_destination_by_season_desert():
    result = suggest_destination_by_season.invoke({"season": "automne", "travel_style": "desert"})
    assert "Merzouga" in result["recommended_destination"] or "Zagora" in result["recommended_destination"]


def test_suggest_destination_by_unknown_style_defaults_to_culture():
    result = suggest_destination_by_season.invoke({"season": "hiver", "travel_style": "luxe"})
    assert result["recommended_destination"] in {"Marrakech, Fes ou Rabat"}
