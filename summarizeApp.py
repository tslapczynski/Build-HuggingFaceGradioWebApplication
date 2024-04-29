from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import gradio as gr

# load model and tokenizer from disk
path = "/home/coder/model/summarizeApp"
model = AutoModelForSeq2SeqLM.from_pretrained(path)
tokenizer = AutoTokenizer.from_pretrained(path)

def summarize(text):
    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

# create an interface for the model
with gr.Interface(summarize, "textbox", "textbox", title="Text Summarization", description="Enter text to summarize:") as interface:
    interface.launch()
