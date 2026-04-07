def apply_action(soil, action):
    if action == 0:
        soil -= 5
    elif action == 1:
        soil += 5
    elif action == 2:
        soil += 10
    elif action == 3:
        soil += 15

    return soil


def apply_weather(soil, weather):
    if weather == "rainy":
        soil += 5
    return soil
