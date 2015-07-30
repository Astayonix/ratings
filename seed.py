"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime

def load_users():
    """Load users from u.user into database."""
    open_file = open("seed_data/u.user")
    for line in open_file:
        listified_user_row = line.strip('\n').split("|")
        user_id = listified_user_row[0]
        age = listified_user_row[1]
        zipcode =listified_user_row[4]
        new_user = User(user_id = user_id, age = age, zipcode = zipcode)
        db.session.add(new_user)
    db.session.commit()


def load_movies():
    """Load movies from u.item into database."""

    open_file = open("seed_data/u.item")
    for line in open_file:
        listified_movie_row = line.split("|")
        movie_id = listified_movie_row[0]
        title = listified_movie_row[1]
        title_stripped = title[:-6]
        released_at = listified_movie_row[2]
        imdb_url = listified_movie_row[4]
        if not released_at:
            continue
        else:
            datetime_released_at = datetime.strptime(released_at, '%d-%b-%Y')
            new_movie = Movie(movie_id=movie_id, title=title_stripped, released_at=datetime_released_at, imdb_url=imdb_url)
            db.session.add(new_movie)
    db.session.commit()


def load_ratings():
    """Load ratings from u.data into database."""
    open_file=open("seed_data/u.data")
    for line in open_file:
        listified_ratings_row = line.split("\t")
        user_id = listified_ratings_row[0]
        movie_id = listified_ratings_row[1]
        score = listified_ratings_row[2]
        new_rating = Rating(user_id=user_id, movie_id=movie_id, score=score)
        db.session.add(new_rating)
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()
