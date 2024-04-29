from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def summarize_text(file_path, model_path):
    # Load pre-trained model and tokenizer from the specified path
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Read text from the specified file
    with open(file_path, encoding="utf-8") as f:
        text = f.read()

    # Tokenize the text and generate a summary using the loaded model
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids)

    # Decode the generated summary
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

if __name__ == "__main__":
    file_path = "text.txt"
    model_path = "/home/coder/model/summarizeApp"
    summary = summarize_text(file_path, model_path)
    print(summary)
