def apply_action(soil, action):
    if action == 0:
        return soil - 5
    elif action == 1:
        return soil + 5
    elif action == 2:
        return soil + 10
    elif action == 3:
        return soil + 15


def apply_weather(soil, weather):
    if weather == "rainy":
        return soil + 5
    elif weather == "cloudy":
        return soil + 2
    elif weather == "foggy":
        return soil + 1
    return soil