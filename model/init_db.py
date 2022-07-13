import sqlite3

conn = sqlite3.connect('./db/database.db')

with open ('./db/schema.sql') as f:
	conn.executescript(f.read())

conn.commit()
conn.close()