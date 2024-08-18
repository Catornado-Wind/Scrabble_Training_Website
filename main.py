from flask import Flask, redirect, render_template, request, url_for, jsonify
import sqlite3 as sql
from queries import rack_query, list_query
import random as r

# app def
app = Flask(__name__)

# list queries
consonants = tuple(letter for letter in "BCDFGHJKLJMNPQRSTVWXYZ")
vowels = tuple(letter for letter in "AEIOU")

word_lists = {
        "2-letter-words": list_query(length=2),
        "3-letter-words": list_query(length=3),
        "4-letter-words": list_query(length=4),
        "5-letter-words": list_query(length=5),
        "6-letter-words": list_query(length=6),
        "7-letter-words": list_query(length=7),
        "8-letter-words": list_query(length=8),
        "9-letter-words": list_query(length=9),
        "10-letter-words": list_query(length=10),
        "11-letter-words": list_query(length=11),
        "12-letter-words": list_query(length=12),
        "13-letter-words": list_query(length=13),
        "14-letter-words": list_query(length=14),
        "15-letter-words": list_query(length=15),
        "Q-words": list_query(contain_letters=("Q",), contains_all=True),
        "Q-without-U-words": list_query(contain_letters=("Q",), contains_all=True, without_letters=("U",)),
        "all-vowel-words": list_query(contain_letters=vowels, contains_all=False, without_letters=consonants),
        "no-vowel-words": list_query(contain_letters=consonants, contains_all=False, without_letters=vowels)
    }

# rack queries
letter_amount = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1,
    # "?": 2
}

letter_bag = []

for letter, number in letter_amount.items():
    letter_bag += [letter] * number


# main
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", word_lists=word_lists.keys())


@app.route("/word_lists", methods=["GET"])
def word_list():
    return render_template("word_list.html", word_lists=word_lists.keys())


@app.route("/word_lists/<word_list>", methods=["GET"])
def words(word_list):

    query = word_lists[word_list]
    
    # connection closes after with block
    with sql.connect("word_list.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute(query)
        words = cursor.fetchall()

    return render_template("words.html",word_lists=word_lists.keys(), word_list=word_list, words=words)


@app.route("/anagrams", methods=["GET", "POST"])
def annagrams():
    # GET
    words_formable = False

    while not words_formable:
        rack = r.choices(letter_bag, k=7)
        rack.sort()

        query = rack_query(rack)
                        
        # connection closes after with block
        with sql.connect("word_list.db") as conn:
            cursor = conn.cursor()
                            
            cursor.execute(query)
            words = cursor.fetchall()

            if len(words) != 0:
                words_formable = True

        answers = [{"answer": word, "revealed": False, "correct": False} for word in words]
        
    # POST
    if request.method == "POST":
        words_formable = False

        while not words_formable:
            rack = r.choices(letter_bag, k=7)
            rack.sort()

            query = rack_query(rack)
            
            # connection closes after with block
            with sql.connect("word_list.db") as conn:
                cursor = conn.cursor()
                
                cursor.execute(query)
                words = cursor.fetchall()

            if len(words) != 0:
                words_formable = True

        answers = [{"answer": word, "revealed": False} for word in words]
    
    
    return render_template("anagrams.html", word_lists=word_lists.keys(), rack=rack, answers=answers)


if __name__ == '__main__':
  app.run(debug=True, port=15003)
