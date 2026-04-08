from fastapi import FastAPI
import random

app = FastAPI()

# Dummy Env
class SmartIrrigationEnv:
    def __init__(self):
        self.moisture = random.randint(30, 70)

    def reset(self):
        self.moisture = random.randint(30, 70)
        return self.moisture

    def step(self, action):
        if action == "water":
            self.moisture += random.randint(5, 15)
        else:
            self.moisture -= random.randint(3, 10)

        self.moisture = max(0, min(100, self.moisture))
        reward = 1 if 40 <= self.moisture <= 70 else -1
        done = False

        return self.moisture, reward, done


env = SmartIrrigationEnv()


@app.get("/")
def home():
    return {"message": "API running"}


@app.post("/step")
def step(action: str):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
