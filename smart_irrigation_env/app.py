import gradio as gr
import random

# Dummy Smart Irrigation Logic (safe version)
class SmartIrrigationEnv:
    def __init__(self):
        self.moisture = random.randint(30, 70)

    def reset(self):
        self.moisture = random.randint(30, 70)
        return self.moisture

    def step(self, action):
        if action == "Water 💧":
            self.moisture += random.randint(5, 15)
        else:
            self.moisture -= random.randint(3, 10)

        self.moisture = max(0, min(100, self.moisture))

        reward = 1 if 40 <= self.moisture <= 70 else -1
        done = False

        return self.moisture, reward, done


env = SmartIrrigationEnv()
state = env.reset()


# FUNCTIONS
def take_action(action):
    global state
    state, reward, done = env.step(action)

    status = "✅ Optimal" if reward == 1 else "⚠️ Not Optimal"

    return f"""
🌿 Soil Moisture: {state}%
🎯 Reward: {reward}
📊 Status: {status}
"""


def reset_env():
    global state
    state = env.reset()
    return f"🔄 Reset Done!\n🌿 Soil Moisture: {state}%"


# UI DESIGN
with gr.Blocks(theme=gr.themes.Soft(), title="Smart Irrigation AI") as demo:

    gr.Markdown(
        """
        # 🌱 Smart Irrigation using Reinforcement Learning
        Control irrigation smartly based on soil moisture levels.
        """
    )

    with gr.Row():
        action = gr.Radio(
            ["Water 💧", "Skip 🚫"],
            label="Choose Action",
            value="Water 💧"
        )

    output = gr.Textbox(label="System Output", lines=5)

    with gr.Row():
        run_btn = gr.Button("🚀 Run Step", variant="primary")
        reset_btn = gr.Button("🔄 Reset")

    run_btn.click(take_action, inputs=action, outputs=output)
    reset_btn.click(reset_env, outputs=output)


demo.launch(server_name="0.0.0.0", server_port=7860)
