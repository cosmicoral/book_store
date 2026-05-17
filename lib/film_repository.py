from lib.film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM films ORDER BY id")
        films = []
        for row in rows:
            film = Film(row["title"], row["release_year"], row["director"], row["id"])
            films.append(film)
        return films
    
    def create(self, film):
        self._connection.execute(
            "INSERT INTO films (title, release_year, director) VALUES(%s, %s, %s)",
            [film.title, film.release_year, film.director]
        )
        