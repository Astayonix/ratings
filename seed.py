"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app

def load_users():
    """Load users from u.user into database."""
    open_file = open("seed_data/u.user")
    for line in open_file:
        listified_user_row = line.split("|").rstrip("\n")
        # print   listified_user_row
        user_id = listified_user_row[0]
        age = listified_user_row[1]
        zipcode =listified_user_row[4]
        new_user = User(user_id = user_id, age = age, zipcode = zipcode)
        db.session.add(new_user)
    db.session.commit()


def load_movies():
    """Load movies from u.item into database."""


def load_ratings():
    """Load ratings from u.data into database."""


if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    # load_movies()
    # load_ratings()
