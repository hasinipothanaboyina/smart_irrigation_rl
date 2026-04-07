def grade(trajectory):
    soil_values = [state["soil_moisture"] for state in trajectory]

    optimal_steps = sum(1 for s in soil_values if 40 <= s <= 70)
    efficiency = optimal_steps / len(soil_values)

    stability = max(soil_values) - min(soil_values)

    return {
        "efficiency_score": round(efficiency, 3),
        "stability_score": round(1 / (1 + stability), 3),
        "message": "Higher efficiency and stability indicate better irrigation strategy."
    }