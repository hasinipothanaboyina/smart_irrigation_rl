import requests

def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=16.3&longitude=80.4&current_weather=true"
        res = requests.get(url, timeout=5).json()

        code = res["current_weather"]["weathercode"]

        # Weather mapping (official)
        if code == 0:
            return "sunny"
        elif code in [1, 2, 3]:
            return "cloudy"
        elif code in [45, 48]:
            return "foggy"
        elif code in [51, 53, 55, 61, 63, 65]:
            return "rainy"
        elif code in [71, 73, 75]:
            return "snow"
        else:
            return "sunny"

    except:
        return "sunny"