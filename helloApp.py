import gradio as gr
from mylib.calculator import add  # Assuming mylib is in the same directory as this file

def calculate(num1, num2):
    result = add(num1, num2)
    return f"The result of {num1} + {num2} is {result}"

with gr.Blocks() as demo:
    num1 = gr.Number(label="Number 1")
    num2 = gr.Number(label="Number 2")
    output = gr.Textbox(label="Result")
    calculate_btn = gr.Button("Calculate")
    calculate_btn.click(fn=calculate, inputs=[num1, num2], outputs=output)

demo.launch()
