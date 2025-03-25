from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)
CORS(app)

def load_model(source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text, source_lang, target_lang):
    try:
        tokenizer, model = load_model(source_lang, target_lang)
        encoded_text = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = model.generate(**encoded_text)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        return translated_text
    except Exception as e:
        return str(e)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    source_lang = data.get("source_lang")
    target_lang = data.get("target_lang")

    if not text or not source_lang or not target_lang:
        return jsonify({"error": "Missing parameters"}), 400

    translated_text = translate_text(text, source_lang, target_lang)
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
