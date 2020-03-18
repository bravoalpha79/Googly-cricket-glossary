import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "Googly"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def index():
    letters = "ABCDEF"
    return render_template("base.html", letters=letters)


@app.route("/display_letter/<letter>")
def display_letter(letter):
    return render_template("letter.html",
                           letter=mongo.db.entries.find({
                            "letter": letter}))


@app.route("/display_word/<word>")
def display_word(word):
    return render_template("word.html",
                           word=mongo.db.entries.find({
                            "term": word}))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
