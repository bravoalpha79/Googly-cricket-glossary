import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask import jsonify
from flask_pymongo import PyMongo
# from bson.json_util import dumps
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "Googly"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@app.route("/")
def index():
    return render_template('index.html', letters=alphabet)


@app.route("/display_letter/<letter>")
def display_letter(letter):
    return render_template("letter.html",
                           letter=mongo.db.entries.find({
                            "letter": letter}).sort("term"), letters=alphabet)

@app.route("/search/<word>")
def search_word(word):
    # saerch in database
    entries = mongo.db.entries
    all_entries = mongo.db.entries.find()
    all_words = [entry["term"] for entry in all_entries]
    glossary = [item.lower() for item in all_words]

    # find if we have the search item in the above said glossary
    found_it = {
        word: 'from glossary you got blah blah blah'
    }
    return jsonify(found_it)

@app.route("/display_word/<word>")
def display_word(word):
    return render_template("word.html",
                           word=mongo.db.entries.find_one({
                            "term": word}), letters=alphabet)


@app.route("/add_word")
def add_word():
    return render_template("addword.html", letters=alphabet)


@app.route("/insert_word", methods=["GET", "POST"])
def insert_word():
    word = request.form["term"]
    entries = mongo.db.entries
    all_entries = mongo.db.entries.find()
    all_words = [entry["term"] for entry in all_entries]
    glossary = [item.lower() for item in all_words]

    meanings = []

    for k, v in request.form.items():
        if k != "term":
            if v != "":
                meanings.append(v)

    if word.lower() in glossary:
        flash(("Entry '{}' already exists.").format(word))
        return redirect(url_for("add_word"))
    else:
        entries.insert_one(
            {
                "term": word,
                "letter": word[0].upper(),
                "meanings": meanings
            })
        flash(("Entry '{}' successfully added.").format(word))
        return redirect(url_for("display_word", word=word))


@app.route("/edit_word/<word_id>")
def edit_word(word_id):
    word_to_edit = mongo.db.entries.find_one({"_id": ObjectId(word_id)})
    return render_template("editword.html",
                           word=word_to_edit, letters=alphabet)


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
def update_word(word_id):
    entries = mongo.db.entries
    all_entries = mongo.db.entries.find()
    all_words = [entry["term"] for entry in all_entries]
    glossary = [item.lower() for item in all_words]

    meanings = []

    for k, v in request.form.items():
        if k != "term":
            if v != "":
                meanings.append(v)

    term_to_update = request.form["term"]

    if term_to_update.lower() in glossary:
        flash(("Entry '{}' already exists.").format(term_to_update))
        return redirect(url_for("edit_word",
                                word_id=word_id))
    else:
        entries.update_one({"_id": ObjectId(word_id)},
                           {"$set": {
                                "term": term_to_update,
                                "meanings": meanings
                           }})
    flash("Word successfully updated.")
    return redirect(url_for("display_word",
                            word=term_to_update))


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    entries = mongo.db.entries
    entries.delete_one({"_id": ObjectId(word_id)})
    flash("Entry successfully deleted.")
    return render_template("addword.html", letters=alphabet)


@app.route("/contribute", methods=["GET", "POST"])
def contribute():
    return render_template("contribute.html", letters=alphabet)


@app.route("/authenticate_user", methods=["GET", "POST"])
def authenticate_user():
    contributors = mongo.db.contributors.find()
    passwords = [entry["passkey"] for entry in contributors]

    if request.method == "POST":
        if request.form["contributor"]:
            if session["username"] == "contributor":
                flash("You are already authorised as contributor")
                return render_template("contribute.html", letters=alphabet)
            elif request.form["contributor"] in passwords:
                session["username"] = "contributor"
                flash("Contributor authorisation successful.")
                return render_template("index.html", letters=alphabet)
            else:
                flash("Authorisation not recognised. Please try again.")
                return render_template("contribute.html", letters=alphabet)


@app.route("/logout")
def logout():
    session["username"] = "guest"
    flash("Successfully logged out.")
    return render_template("index.html", letters=alphabet)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
