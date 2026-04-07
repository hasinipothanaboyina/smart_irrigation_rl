import gradio as gr
from env import Env

env = Env()
state = env.reset()

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