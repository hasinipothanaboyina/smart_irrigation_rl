from utils.reward import compute_reward
from utils.dynamics import apply_action, apply_weather
from utils.weather_api import get_weather  # 🔥 real-time weather
import random


class Env:
    def __init__(self):
        self.max_steps = 30
        self.reset()

    def reset(self):
        self.soil = random.randint(30, 70)

        # 🌍 Real-time weather (fallback if error)
        try:
            self.weather = get_weather()
        except:
            self.weather = "sunny"

        self.step_count = 0
        return self._get_state()

    def _get_state(self):
        return {
            "soil_moisture": self.soil,
            "weather": self.weather
        }

    def step(self, action):
        self.step_count += 1

        # Apply irrigation action
        self.soil = apply_action(self.soil, action)

        # Apply weather effect
        self.soil = apply_weather(self.soil, self.weather)

        # Clamp values
        self.soil = max(0, min(100, self.soil))

        # Reward calculation
        reward, status = compute_reward(self.soil)

        done = self.step_count >= self.max_steps

        return self._get_state(), reward, done, {"status": status}