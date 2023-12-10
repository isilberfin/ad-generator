import io
from flask import Flask, request, render_template_string
import joblib
import img_generate_inference
import create_card
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/generateCard', methods=['POST'])
def generate_card_controller():
    sample_photo = request.files['samplePhoto'].read()
    logo_photo = request.files['logoPhoto'].read()
    prompt = request.form.get('prompt')
    color = request.form.get('color')
    punchline_color = request.form.get("punchlineColor")
    punchline_text = request.form.get("punchlineText")
    button_text = request.form.get("buttonText")

    #punchline_color = request.form.get('punchlineColor')
    #punchline_text = request.form.get('punchlineText')
    img_generate_inference.generate_img(sample_photo, prompt, color)
    photo = create_card.generate_card(logo_photo,punchline_color,punchline_text,button_text)

    # Return the image as the response
    return render_template_string(photo)
    


