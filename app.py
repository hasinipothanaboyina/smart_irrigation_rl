import gradio as gr
from env import Env

env = Env()
state = env.reset()

def run_step():
    global state
    action = 2
    state, reward, done, info = env.step(action)

    return (
        state["soil_moisture"],
        state["weather"],
        reward,
        info["status"]
    )

gr.Interface(
    fn=run_step,
    inputs=[],
    outputs=["number", "text", "number", "text"],
    title="🌱 Smart Irrigation RL"
).launch()