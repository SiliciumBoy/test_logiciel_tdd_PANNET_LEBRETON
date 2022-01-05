DROP TABLE IF EXISTS Utilisateur;

-- CREATE TABLE Utilisateur (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL check(length(username) >= 4),
-- 			password TEXT NOT NULL check(length(password) > 8), spublickey TEXT NOT NULL check(length(spublickey) == 128), 
-- 			sprivatekey TEXT NOT NULL check(length(sprivatekey) == 128), epublickey TEXT NOT NULL check(length(epublickey) == 128),
-- 			eprivatekey TEXT NOT NULL check(length(eprivatekey) == 128));

CREATE TABLE Utilisateur (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE check(length(username) >= 4), pass_word TEXT NOT NULL check(length(pass_word) > 8));