# Import module
from flask import Flask, render_template

# app devient notre server
app = Flask(__name__)

# Création d'une route "/"
@app.route("/")
def helloWorld(): # La fonction de notre route
    return "Hello, World!"

# Notre route "/hello"
@app.route("/hello")
def hello():
    return render_template("index.html") # renvoie de notre page html

if __name__ == '__main__':
   app.run(debug = True)
