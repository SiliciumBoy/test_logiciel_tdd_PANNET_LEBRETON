import sqlite3
import funcs
import unittest
from dbsql import *
# from dbsql import add_user
# from dbsql import login
from sqlite3 import IntegrityError

class TestFuncs(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect('exercice2.db')
		self.conn.row_factory = sqlite3.Row
		self.cursor = self.conn.cursor()
		delete(self.cursor)
		self.cursor("CREATE TABLE Utilisateur (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE check(length(username) >= 4), pass_word TEXT NOT NULL check(length(pass_word) > 8));")
		add_user(self.cursor, 'pilouf', 'jesuisuneetoale')
		add_user(self.cursor, 'jeanne', '123456789')


	def test_add_user(self):
		# add_user(self.cursor, 'pumba', 'ozfe')
		with self.assertRaises(IntegrityError):
			add_user(self.cursor, 'oie', 'ozfeddddddd')

	def test_login(self):
		self.assertEqual(login(self.cursor, 'jeanne', '123456789'), True)
		self.assertEqual(login(self.cursor, 'pilouf', 'jesuisuneetoale'), True)
		self.assertEqual(login(self.cursor, 'pilouf', 'jesuisunetoale'), False)
		self.assertEqual(login(self.cursor, 'jeanne', 'jesuisuneetoale'), False)

	# def test_corrompu(self):
	# 	for i in range(0, 3):
	# 		self.assertEqual(corrompu(self.cursor, i))

	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
	unittest.main()