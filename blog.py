import os
import csv
import pandas as pd
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import CreateForm
from datetime import datetime

#A function to check if such file exists, if not, one will be created and populated with column names
if not os.path.exists("restaurant_reviews.csv"): 

    fieldnames = ["ID","Restaurant_Name", "Rating", "Review_Text", "Date"] 

    with open ("restaurant_reviews.csv", "w") as reviews:
        writer = csv.DictWriter(reviews, fieldnames = fieldnames)
        writer.writeheader()
    
    

app = Flask(__name__) 

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#The home route which displays all items in the csv file in reverse chronological order 
@app.route("/")
@app.route("/reviews")
def index():
    with open("restaurant_reviews.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        reviews = list(reader)
        reviews.reverse()
        return render_template("index.html", reviews=reviews)

    
#The about route to briefly explain the purpose of this web application
@app.route("/about")
def about():
    return render_template("about.html")


#The show route which displays each review in detail 
@app.route("/reviews/<int:ID>")
def show(ID):
    with open("restaurant_reviews.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        reviews = list(reader)
        for review in reviews:
            if int(review["ID"]) == ID:
                return render_template("show.html", review=review)
        return "<h1>This review does not exist<h1>"


#The create route which displays a form in order to add a review and accept a post request when the form is submitted     
@app.route("/reviews_post", methods=['GET','POST'])
def create():
    form = CreateForm()
    
    restaurant_name = request.form.get("restaurant_name")
    rating = request.form.get("rating")
    review_text = request.form.get("review_text")
    current_date = datetime.now().strftime('%d-%m-%Y')
    
    if restaurant_name and rating and review_text:
    
        with open ("restaurant_reviews.csv", "r") as csv_file:
            reader = csv.DictReader(csv_file)
            length = len(list(reader))
            new_review = {"ID": length+1,"Restaurant_Name":restaurant_name , "Rating":rating, "Review_Text":review_text, "Date":current_date}

            fieldnames = ["ID","Restaurant_Name", "Rating", "Review_Text", "Date"]

            with open ("restaurant_reviews.csv", "a") as reviews:
                writer = csv.DictWriter(reviews, fieldnames = fieldnames)
                writer.writerow(new_review)
            
            flash('Your review has been posted!')

            return redirect(url_for("index"))
    return render_template("create.html", form=form)

            
if __name__ == '__main__':
    app.run()