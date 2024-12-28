import gradio as gr
import agent
import asyncio

def main(prompt):
    try:
        result = asyncio.run(agent.run(prompt))
        return result
    except agent.AgentError as e:
        return ''

with gr.Blocks() as app:
    input = gr.Textbox(lines=2, placeholder='Enter your prompt here...')
    output = gr.Textbox(lines=5)

    input.submit(main, inputs=input, outputs=output)

if __name__ == '__main__':
    app.launch()
