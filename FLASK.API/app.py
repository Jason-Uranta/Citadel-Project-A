from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Grad our data
    apikey = ""
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto" + "?apikey=" + apikey)
    # transform to JSON format (similar to a nested dictionary)
    data = response.json()
    img = data["sprites"]["front_default"]
    name = data["forms"][0]["name"]
    return render_template("index.html", poke_src=img, poke_name=name)

if __name__ == "__main__":
    app.run()