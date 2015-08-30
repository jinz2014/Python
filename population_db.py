import sqlite3

con = sqlite3.connect('population.db')

cur = con.cursor()

# 
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGR)')

cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
cur.execute('INSERT INTO PopByRegion VALUES(?, ?)', ("Eastern Asia", 1362955))

con.commit()

cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
print(cur.fetchall())

cur.execute('SELECT Region FROM PopByRegion WHERE Population > 100000')
cur.fetchone()

cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
cur.fetchone()

cur.execute('UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"')
cur.fetchone()

# Use NULL to indicate missing population
cur.execute('INSERT INTO PopByRegion VALUES("Mars", NULL)')

# delete the table
cur.execute('DROP TABLE PopByRegion')
