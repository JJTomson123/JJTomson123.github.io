import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from __init__ import app





@app.route("/")
@app.route("/index")
def home():
    return  render_template("index.html")


@app.route("/hobbies")
def about():
    return render_template("Hobbies.html", title='Hobbies')


