from flask import Flask, render_template, request, flash
from forms import CreateForm

reviews = [
    {"book_title":"Confessions of a Python Programmer", "review_text":"A cautionary tale for all would-be programmers", "score":5, "id":"1"},
    {"book_title":"To Serve Man", "review_text":"Delicious recipes", "score":3, "id":"2"},
    {"book_title":"Pride and Prejudice", "review_text":"The pride is ok but the prejudice not so much", "score":4, "id":"3"},
]

app = Flask(__name__) 


@app.route("/reviews/<ID>")
def show(ID):
    for review in reviews:
        if review['id'] == str(ID):
            return render_template("show.html", review = review, reviews = reviews)
        else:
            return "<h1>This Review ID Does Not Exist<h1>"

@app.route("/")
@app.route("/reviews")
def index():
    return render_template("index.html", reviews=reviews)


@app.route("/reviews", methods=['POST'])

def create():
    form = CreateForm()
    flash('Your review has been created!')
    return render_template("create.html", title='New Review', form=form)

if __name__ == 'main':
    app.run(debug=True)