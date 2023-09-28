# Web Scraping
# install new library on google colab
# pip => package manager in Python

!pip install gazpacho

## import function
from gazpacho import Soup
import requests

## web scraping basics
url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
html = requests.get(url) ## Accept-Language: en
imdb = Soup(html.text)

## list comprehension

## get header from the website
## h3: lister-item-header
titles = imdb.find("h3", {"class": "lister-item-header"})
clean_titles = [title.strip() for title in titles]

## get rating from the website
## div: rating-imdb-rating
ratings = imdb.find("div", {"class": "ratings-imdb-rating"})
clean_ratings = [float(rating.strip()) for rating in ratings]

## get year from the website
## span: lister-item-year
years = imdb.find("span", {"class": "lister-item-year"})
clean_year = [year.strip().replace("(", "").replace(")", "") for year in years]

import pandas as pd
movie_database = pd.DataFrame(data = {
    "title": clean_titles,
    "rating" : clean_ratings,
    "year" : clean_year
})

# print first ten rows
movie_database.head(10)
