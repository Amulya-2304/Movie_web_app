from flask import Flask, render_template, request, redirect, url_for
import json
import os
import webbrowser
import threading

app = Flask(__name__)
DATA_FILE = 'movies.json'


# Load movies from file
def load_movies():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


# Save movies to file
def save_movies(movies):
    with open(DATA_FILE, 'w') as f:
        json.dump(movies, f, indent=4)


@app.route('/')
def home():
    movies = load_movies()
    return render_template('index.html', movies=movies)


@app.route('/add', methods=['POST'])
def add_movie():
    title = request.form['title']
    year = request.form['year']
    genre = request.form['genre']

    if title and year and genre:
        movies = load_movies()
        movies.append({'title': title, 'year': year, 'genre': genre})
        save_movies(movies)
    return redirect(url_for('home'))


@app.route('/delete/<int:index>')
def delete_movie(index):
    movies = load_movies()
    if 0 <= index < len(movies):
        movies.pop(index)
        save_movies(movies)
    return redirect(url_for('home'))


# Automatically open in browser
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)
