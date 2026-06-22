# Import
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# Página principal
@app.route('/')
def index():
    return render_template('index.html')


# Procesar selección de habilidad (POST desde Skills)
@app.route('/', methods=['POST'])
def process_form():
    # ✏️ Recibe qué habilidad seleccionó el usuario y la manda al template
    skill_selected = request.form.get('skill_selected')
    return render_template('index.html', skill_selected=skill_selected)


if __name__ == "__main__":
    app.run(debug=True)
