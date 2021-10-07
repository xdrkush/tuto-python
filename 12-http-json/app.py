# save this as app.py
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def user():
    # Récupération du fichier json dans l'architecture
    user = open('static/user.json',)
    # Chargement du fichier json
    data = json.load(user)
    # Renvoi de la response
    return jsonify(data)

if __name__ == '__main__':
   app.run(debug = True)