-- create a new database and create a table in  the data base
CREATE DATABASE IF NOT EXISTs hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE, name VARCHAR(256) NOT NULL);
