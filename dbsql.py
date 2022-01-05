import sqlite3, random

# ouverture/initialisation de la base de donnee 
conn = sqlite3.connect('exercice2.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

def add_user(cursor, username, password):
	if len(password) < 8 or len(username) < 3 :
		print("Username: Plus de 3 caracteres; Password: plus de 8 caracteres")
		return
	cursor.execute("INSERT INTO Utilisateur (username, pass_word) VALUES (?, ?);", (username, password))

def login(cursor, username, password):
	rows = cursor.execute("SELECT username, pass_word FROM Utilisateur WHERE username =? AND pass_word =?", (username, password)).fetchall()
	if rows:
		return True
	return False

# def corrumpu(cursur, id):

def delete(cursor):
	cursor.execute("DELETE FROM Utilisateur")

# fermeture
conn.commit()
conn.close()