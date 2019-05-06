# mswipe
RESTful API for movies(something similar to IMDB).

use:

1. MySql or SQLlite to store data

2. Any Python Framework for implementing the APIs.

There need to be 2 levels of access:

admin = who can add, remove or edit movies.

users = who can just view the movies.



● There should also be a decent implementation to search for movies.

● Document your code well so that we can test the API with ease.

● For your convenience I have attached some data that you can use to populate your

database.

● Try and deploy this on Heroku.

############################################################################################
API request examples:

base API - https://mswipemovies.herokuapp.com/api/movies

filter by name (full text search) - https://mswipemovies.herokuapp.com/api/movies?name=wizard

filter by movie name and director name - https://mswipemovies.herokuapp.com/api/movies?name=wizard&director=victor

filter by genre name - https://mswipemovies.herokuapp.com/api/movies?genre=family

Admin-panel - https://mswipemovies.herokuapp.com/admin

# Setting up project and initializing data

create a virtualenv 

virtualenv env

cd env

./Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

python manage.py populate_movies
