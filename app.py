import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "Googly"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# constants created to avoid repetition in code

# constant for letter navigation
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

DB = mongo.db


@app.route("/")
def index():
    return render_template('index.html', letters=ALPHABET)


@app.route("/display_letter/<letter>")
def display_letter(letter):
    """Display links to all words starting with selected letter."""
    return render_template("letter.html",
                           index=DB.entries.find({
                            "letter": letter}).sort("term"),
                           letter=letter,
                           letters=ALPHABET)


@app.route("/find_words", methods=["GET", "POST"])
def find_words():
    """Find and display word(s) matching a searchbox query."""
    entries = DB.entries
    all_entries = entries.find()
    # list comprehension method obtained from datacamp.com
    all_words = [item["term"] for item in all_entries]

    search_term = request.form["search"]

    matches = []

    for entry in all_words:
        if search_term and entry[0:len(search_term)] == search_term:
            matches.append(entry)

    return render_template("search.html", letters=ALPHABET,
                           matches=matches, search_term=search_term)


@app.route("/display_word/<word>")
def display_word(word):
    """Display full entry details of selected word."""
    return render_template("word.html",
                           word=DB.entries.find_one({
                            "term": word}), letters=ALPHABET)


@app.route("/add_word")
def add_word():
    """Display form for adding new word."""
    return render_template("addword.html", letters=ALPHABET)


@app.route("/insert_word", methods=["GET", "POST"])
def insert_word():
    """Process addword form and insert word into DB."""
    word = request.form["term"]
    entries = DB.entries
    all_entries = DB.entries.find()
    all_words = [entry["term"] for entry in all_entries]
    glossary = [item.lower() for item in all_words]

    meanings = []

    #check if first character is a letter    
    if word[0].upper() not in ALPHABET:   
        flash("A word must start with a letter.")
        return redirect(url_for("add_word"))
    
    # key-value iteration code obtained from W3Schools.com
    for k, v in request.form.items():
        if k != "term":
            if v != "":
                meanings.append(v)
    # check if same word already exists in DB
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
    """ Display editword form for selected word"""
    word_to_edit = DB.entries.find_one({"_id": ObjectId(word_id)})
    return render_template("editword.html",
                           word=word_to_edit, letters=ALPHABET)


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
def update_word(word_id):
    """Process editword form and insert update(s) into DB"""
    entries = DB.entries
    term_to_update = request.form["term"].lower()
    same_term = entries.find_one({"term": term_to_update})

    meanings = []
    # key-value iteration code obtained from W3Schools.com
    for k, v in request.form.items():
        if k != "term":
            if v != "":
                meanings.append(v)
    # if word (term) is modified, check if same entry already exists in DB
    if same_term and same_term["_id"] != ObjectId(word_id):
        flash(("Entry '{}' already exists.").format(term_to_update))
        return redirect(url_for("edit_word",
                                word_id=word_id))
    else:
        entries.update_one({"_id": ObjectId(word_id)},
                           {"$set": {
                                "term": term_to_update,
                                "letter": term_to_update[0].upper(),
                                "meanings": meanings
                           }})
    flash("Word successfully updated.")
    return redirect(url_for("display_word",
                            word=term_to_update))


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    """Delete selected entry from DB."""
    entries = DB.entries
    entries.delete_one({"_id": ObjectId(word_id)})
    flash("Entry successfully deleted.")
    return render_template("addword.html", letters=ALPHABET)


@app.route("/contribute", methods=["GET", "POST"])
def contribute():
    return render_template("contribute.html", letters=ALPHABET)


@app.route("/authenticate_user", methods=["GET", "POST"])
def authenticate_user():
    """Process contributor authorisation form."""
    contributors = DB.contributors.find()
    passwords = [entry["passkey"] for entry in contributors]

    if request.method == "POST":
        # check if contributor is already logged in
        if "username" in session:
            flash("You are already authorised as contributor")
            return render_template("contribute.html", letters=ALPHABET)
        # check if password exists in DB
        elif request.form["contributor"] in passwords:
            session["username"] = "contributor"
            flash("Contributor authorisation successful.")
            return render_template("index.html", letters=ALPHABET)
        else:
            flash("Authorisation not recognised. Please try again.")
            return render_template("contribute.html", letters=ALPHABET)


@app.route("/logout")
def logout():
    """Log out contributor."""
    if "username" not in session:
        return render_template("index.html", letters=ALPHABET)
    # session.pop method obtained from Stack Overflow
    else:
        session.pop("username")
        flash("Successfully logged out.")
        return render_template("index.html", letters=ALPHABET)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
