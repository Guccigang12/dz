import sqlite3
conn = sqlite3.connect('data1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS People (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')
people_data = [
    ('Timyr', 11),
    ('Artyr', 11),
    ('Myrmyr', 11)
]
cursor.execute('INSERT INTO People (name, age) VALUES (?, ?)', people_data)
conn.commit()
cursor.execute('SELECT * FROM People')
ryadoks = cursor.fetchall()
for ryadok in ryadoks:
    print(ryadok)
conn.close()
