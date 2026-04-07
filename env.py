from utils.reward import compute_reward
from utils.dynamics import apply_action, apply_weather
import random


class Env:
    def __init__(self):
        self.max_steps = 30
        self.reset()

    def reset(self):
        self.soil = random.randint(30, 70)
        self.weather = random.choice(["sunny", "rainy"])
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

        # Apply weather impact
        self.soil = apply_weather(self.soil, self.weather)

        # Clamp values
        self.soil = max(0, min(100, self.soil))

        # Compute reward
        reward, status = compute_reward(self.soil)

        done = self.step_count >= self.max_steps

        return self._get_state(), reward, done, {"status": status}


# 🔥 TEST BLOCK (VERY IMPORTANT)
if __name__ == "__main__":
    env = Env()
    state = env.reset()

    print("🌱 Smart Irrigation Simulation\n")
    print("Initial State:", state)

    for i in range(5):
        action = 2  # medium water
        state, reward, done, info = env.step(action)

        print(f"\nStep {i+1}")
        print("State:", state)
        print("Reward:", reward)
        print("Status:", info["status"])