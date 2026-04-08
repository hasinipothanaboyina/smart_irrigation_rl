import gradio as gr
from env import Env
from fastapi import FastAPI

# Initialize
env = Env()
state = env.reset()

# -------------------------
# 🌐 FASTAPI (Backend API)
# -------------------------
app = FastAPI()

@app.post("/openenv/reset")
def reset_env():
    global state
    state = env.reset()
    return state

@app.post("/openenv/step")
def step_env(action: int = 2):
    global state
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "status": info["status"]
    }

# -------------------------
# 🎨 GRADIO UI
# -------------------------
def run_step(action):
    global state
    state, reward, done, info = env.step(action)

    return (
        state["soil_moisture"],
        state["weather"],
        reward,
        info["status"]
    )

with gr.Blocks() as demo:
    gr.Markdown("# 🌱 Smart Irrigation RL")

    action_input = gr.Dropdown(
        choices=[0,1,2,3],
        label="Select Irrigation Level",
        value=2
    )

    output1 = gr.Number(label="Soil Moisture")
    output2 = gr.Textbox(label="Weather")
    output3 = gr.Number(label="Reward")
    output4 = gr.Textbox(label="Status")

    btn = gr.Button("Run Step")

    btn.click(
        fn=run_step,
        inputs=[action_input],
        outputs=[output1, output2, output3, output4]
    )

demo.launch()
