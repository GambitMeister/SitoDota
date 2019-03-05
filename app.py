from flask import Flask, render_template
import requests
import pandas as pd
import json

app = Flask(__name__)

hData = pd.DataFrame(requests.get("https://api.opendota.com/api/heroStats").json())

@app.route("/")
def index():
    return render_template("home.html", data = hData)

if __name__ == "__main__":
    app.run(debug = True)