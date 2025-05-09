from abc import ABC, abstractmethod

class DataManager(ABC):
    """
    Abstract base class for data managers that defines the required methods for handling data.
    """

    @abstractmethod
    def add_user(self, username, email):
        """
        Adds a user to the data source.
        :param username: The username of the new user.
        :param email: The email of the new user.
        """
        pass

    @abstractmethod
    def get_all_users(self):
        """
        Retrieves all users from the data source.
        :return: A list of users.
        """
        pass

    @abstractmethod
    def add_movie(self, user_id, movie_name, genre, rating):
        """
        Adds a new movie to the user's favorite list.
        :param user_id: The ID of the user.
        :param movie_name: The name of the movie.
        :param genre: The genre of the movie.
        :param rating: The rating of the movie.
        """
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """
        Retrieves the list of movies for a specific user.
        :param user_id: The ID of the user.
        :return: A list of movies for the user.
        """
        pass

    @abstractmethod
    def update_movie(self, movie_id, movie_name, genre, rating):
        """
        Updates an existing movie's details.
        :param movie_id: The ID of the movie to update.
        :param movie_name: The new movie name.
        :param genre: The new genre.
        :param rating: The new rating.
        """
        pass

    @abstractmethod
    def delete_movie(self, movie_id):
        """
        Deletes a movie from the data source.
        :param movie_id: The ID of the movie to delete.
        """
        pass
