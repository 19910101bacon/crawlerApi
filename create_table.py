import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

### users
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

### items
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, amount int, first_day text, last_day text)"
cursor.execute(create_table)

### articles
create_table = "CREATE TABLE IF NOT EXISTS articles (id text PRIMARY KEY, title text, context text)"
cursor.execute(create_table)

connection.commit()
connection.close()
