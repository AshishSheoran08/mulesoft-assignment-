import sqlite3

conn = sqlite3.connect('moviestable.db')

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE movie (
	movie_name text,
	actor_name text,
	actress_name text,
	year_released int,
	director_name text
	)""")

many_movie = 	[
			('Amazing Spider Man', 'Andrew Garfield', 'Emma Stone', '2012', 'Marc Webb'),
			('Avengers Endgame', 'Robert', 'Scarlett Johnson', '2019', 'Anthony Russo'),
			('RRR', 'Ram Charan', 'Alia Bhatt', '2022', 'SS Rajamouli'),
			('Kashmir Files', 'Darshan Kumar', 'Pallavi Joshi', '2022', 'Vivek Agnihotri'),
			('Student of the year', 'Siddarth Malhotra', 'Alia Bhatt', '2016', 'Karan Johar'),
		]

cursor.executemany("INSERT INTO movie VALUES (?,?,?,?,?)", many_movie)

cursor.execute("SELECT * FROM movie")

items = cursor.fetchall()

for item in items:
	print(item)

print("------------------------")

cursor.execute("SELECT * FROM movie WHERE actor_name='Andrew Garfield'")
print("Your search for actor is")
print(cursor.fetchone())

conn.commit()

conn.close()
