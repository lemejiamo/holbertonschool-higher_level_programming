-- create table cities
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, 
	state_id INTEGER,
	FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);

