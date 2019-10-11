import sqlite3
db = sqlite3.connect("world.db")
x = db.cursor()
x.execute("SELECT name FROM country WHERE population > 100000000")
print(x.fetchall())
x.execute("SELECT name FROM country WHERE name like '%land'")
print(x.fetchall())
x.execute("SELECT name FROM city WHERE Population BETWEEN 500000 and 1000000")
print(x.fetchall())
x.execute("SELECT name FROM country WHERE Continent = 'Europe'")
print(x.fetchall())
x.execute("SELECT name FROM country ORDER BY SurfaceArea DESC")
print(x.fetchall())
x.execute("SELECT name FROM city WHERE CountryCode = 'NLD'")
print(x.fetchall())
x.execute("SELECT Population FROM city WHERE name = 'Amsterdam'")
print(x.fetchall())
x.execute("SELECT city.name FROM city INNER JOIN country on city.CountryCode = country.Code WHERE Continent = 'Europe' ORDER BY city.Population DESC LIMIT 1")
print(x.fetchall())
x.execute("SELECT name FROM country WHERE Continent = 'Africa' ORDER BY SurfaceArea DESC LIMIT 1")
print(x.fetchall())
x.execute("SELECT name FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 10")
print(x.fetchall())
x.execute("SELECT name FROM country ORDER BY SurfaceArea LIMIT 1")
print(x.fetchall())
x.execute("SELECT name FROM city ORDER BY Population DESC LIMIT 10")
print(x.fetchall())
x.execute("SELECT sum(population) FROM country ")
print(x.fetchall())