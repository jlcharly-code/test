
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys   
from flask import Flask, render_template   
from dotenv import load_dotenv
load_dotenv()  # charge .env automatiquement

import os
DATABASE_URL = os.environ["DATABASE_URL"]



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

# Config inline
app.config["DATABASE_URL"] = os.environ["DATABASE_URL"]
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["CLOUDINARY_URL"] = os.environ["CLOUDINARY_URL"]

def main(args):
    app.run(host='127.0.0.1', port=5000, debug=True)
    return 0

