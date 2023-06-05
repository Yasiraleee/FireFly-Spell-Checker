from flask import Flask,render_template,request,url_for,flash
import nltk
import json
import sys
from nltk.corpus import wordnet
import re
from nltk.corpus import words
from textblob import TextBlob
import spacy
nlp = spacy.load("en_core_web_sm")
nltk.download("words")
nltk.download('wordnet')

app = Flask(__name__)
def check_spelling(content):
    misspelled = []
    for word in content.split():
        print(word)
        if re.sub(r"[^\w]", "", word.lower()) not in words.words():
            misspelled.append(word)
    return misspelled

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/api/check",methods=['POST'])
def func():
    data=request.get_json()
    print(data["title"])
    phrase = data["title"]
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    synonyms = list(dict.fromkeys(synonyms))
    antonyms = list(dict.fromkeys(antonyms))
    d={"synonymns":synonyms,
       "antonyms":antonyms
       }
    return  json.dumps(d)

@app.route("/api/spell_checker", methods=["POST"])
def spellCheck():
    data=request.get_json()
    content = data["title"]
    print(content)
    var=str(content)
    misspelled = check_spelling(content)
    correction = ""
    corrections = []
    ccsentence=""
    if misspelled:
        print("Misspelled words: ", ", ".join(misspelled))
        if misspelled:
            for word in misspelled:
                correction = TextBlob(word).correct()
                print(f"{word} -> {correction}")
                corrections.append(str(correction))
                var=var.replace(str(word),str(correction))
                print(var)
    else:
        print("No misspelled words.")
    print(str(correction))
    count=len(corrections)
    myDict = {
        "mispelled": misspelled,
        "correction": corrections,
        "count":count,
        "ccsentence":var
    }
    return json.dumps(myDict)

@app.route("/api/similarity", methods=["POST"])
def similarity():
    data = request.get_json()
    content = data["title"]
    content2 = data["title2"]
    synset1 = wordnet.synsets(content)[0]
    synset2 = wordnet.synsets(content2)[0]
    similarity = synset1.wup_similarity(synset2)
    print(similarity)
    if similarity<=0.7:
        similarity1="Not Similar To Each Other!"
    else:
        similarity1="Similar"
    myd = {
        "percentage": similarity,
        "similarity": similarity1
    }
    return json.dumps(myd)

@app.route("/api/poss", methods=["POST"])
def poss():
    data = request.get_json()
    content = data["title"]
    count = len(content.split())
    noun = []
    adj = []
    punc = []
    preposition = []
    pron = []
    VERB = []
    ADVERB = []
    CONJ = []
    doc = nlp(content)
    for token in doc:
        if token.pos_ == "NOUN":
            noun.append(token.text)
        elif token.pos_ == "ADJ":
            adj.append(token.text)
        elif token.pos_ == "ADP":
            preposition.append(token.text)
        elif token.pos_ == "PUNCT":
            punc.append(token.text)
        elif token.pos_ == "PRON":
            pron.append(token.text)
        elif token.pos_ == "VERB":
            VERB.append(token.text)
        elif token.pos_ == "ADV":
            ADVERB.append(token.text)
        elif token.pos_ == "CCONJ" or token.pos_ == "SCONJ":
            CONJ.append(token.text)

    noun = list(set(noun))
    adj = list(set(adj))
    preposition = list(set(preposition))
    punc = list(set(punc))
    pron = list(set(pron))
    VERB = list(set(VERB))
    ADVERB = list(set(ADVERB))
    CONJ = list(set(CONJ))
    myd = {
        "count":count,
        "noun": noun,
        "pronoun": pron,
        "verb": VERB,
        "adjective": adj,
        "adverb": ADVERB,
        "preposition": preposition,
        "conjunction": CONJ,
        "punction": punc
    }
    return json.dumps(myd)

if __name__ == "__main__":
    app.run(debug=True)

