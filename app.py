from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connexion à la base
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Page d'accueil
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Route pour ajouter un utilisateur
@app.route('/add', methods=['POST'])
def add():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
