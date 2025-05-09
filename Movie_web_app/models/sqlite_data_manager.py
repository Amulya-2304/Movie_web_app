import sqlite3
from .data_manager_interface import DataManager

class SQLiteDataManager(DataManager):
    """
    SQLite Data Manager class that implements the methods to interact with the SQLite database.
    """

    def __init__(self, db_path):
        """
        Initializes the SQLiteDataManager with the database path.
        :param db_path: The path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None  # SQLite connection object

    def connect(self):
        """
        Connects to the SQLite database.
        :return: SQLite connection object.
        """
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def close(self):
        """
        Closes the SQLite database connection.
        """
        if self.connection:
            self.connection.close()

    def add_user(self, username, email):
        """
        Adds a new user to the database.
        :param username: The username of the new user.
        :param email: The email of the new user.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
        conn.commit()
        self.close()

    def get_all_users(self):
        """
        Retrieves all users from the database.
        :return: A list of users.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        self.close()
        return users

    def add_movie(self, user_id, movie_name, genre, rating):
        """
        Adds a new movie to a user's favorite list.
        :param user_id: The ID of the user.
        :param movie_name: The name of the movie.
        :param genre: The genre of the movie.
        :param rating: The rating of the movie.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies (user_id, movie_name, genre, rating) VALUES (?, ?, ?, ?)",
                       (user_id, movie_name, genre, rating))
        conn.commit()
        self.close()

    def get_user_movies(self, user_id):
        """
        Retrieves the list of movies for a specific user.
        :param user_id: The ID of the user.
        :return: A list of movies for the user.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE user_id = ?", (user_id,))
        movies = cursor.fetchall()
        self.close()
        return movies

    def update_movie(self, movie_id, movie_name, genre, rating):
        """
        Updates the details of an existing movie.
        :param movie_id: The ID of the movie to update.
        :param movie_name: The new movie name.
        :param genre: The new genre.
        :param rating: The new rating.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE movies SET movie_name = ?, genre = ?, rating = ? WHERE movie_id = ?",
                       (movie_name, genre, rating, movie_id))
        conn.commit()
        self.close()

    def delete_movie(self, movie_id):
        """
        Deletes a movie from the user's favorite list.
        :param movie_id: The ID of the movie to delete.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE movie_id = ?", (movie_id,))
        conn.commit()
        self.close()
