from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "ITSASECRET"

debug = DebugToolbarExtension

first_story = Story(['place', 'noun', 'verb', 'adjective'],
"""A long, long time ago in {place} there lived a large {adjective} {noun}. 
Its favorite activity was to {verb}.""")

second_story = Story(['verb', 'noun', 'adverb', 'food'],
"""The clown from the circus loved to {verb} the {noun}. One time he {adverb} messed
up and the {food} landed on his face to everyone's joy""")

@app.route("/")
def home():
    """Home screen where you select which story to produce"""
    return render_template('home.html')

@app.route("/form1")
def generate_form1():
    """form to generate story 1"""
    prompts = first_story.prompts
    return render_template("form1.html", prompts=prompts)

words = {}
@app.route("/firststory", methods=['POST'])
def show_first_story():
    """returns a story with user inputs"""
    words['place'] = request.form['place']
    words['noun'] = request.form['noun']
    words['verb'] = request.form['verb']
    words['adjective'] = request.form['adjective']
    
    newStory = first_story.generate(words)
    return render_template("story.html", story=newStory)


@app.route("/form2")
def generate_form2():
    """form to generate story 2"""
    prompts = second_story.prompts
    return render_template("form2.html", prompts=prompts)

@app.route("/secondstory", methods=['POST'])
def show_second_story():
    """return a second story with user inputs"""
    words['verb'] = request.form['verb']
    words['noun'] = request.form['noun']
    words['adverb'] = request.form['adverb']
    words['food'] = request.form['food']
    
    newStory = second_story.generate(words)
    return render_template("story.html", story=newStory)
