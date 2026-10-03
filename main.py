#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()  # charge .env automatiquement

app = Flask(__name__)

# Config (os.environ.get évite un plantage si une variable manque)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")
app.config["CLOUDINARY_URL"] = os.environ.get("CLOUDINARY_URL")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/le-livre")
def le_livre():
    return render_template("le_livre.html")

@app.route("/the-book")
def the_book():
    return render_template("the_book.html")

@app.route("/el-libro")
def el_libro():
    return render_template("el_libro.html")

@app.route("/o-sepulcro")
def o_sepulcro():
    return render_template("o_livro.html")

@app.route("/templiers")
def templiers():
    return render_template("templiers.html")

@app.route("/memoires")
def memoires():
    return render_template("memoires.html")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(app.root_path, "sitemap.xml", mimetype="application/xml")

@app.route("/robots.txt")
def robots():
    return send_from_directory(app.root_path, "robots.txt", mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
