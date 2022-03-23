import sqlite3

conn = sqlite3.connect('moviestable.db')

cursor = conn.cursor()

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