from lib.film import Film
from lib.film_repository import FilmRepository

def test_get_all_films(db_connection):
    db_connection.seed("seeds/films.sql")
    repository = FilmRepository(db_connection)

    films = repository.all()

    assert films ==[Film("In the Mood for Love", 2000, "Wong Kar-wai", 1),
        Film("Chungking Express", 1994, "Wong Kar-wai", 2),
        Film("Spirited Away", 2001, "Hayao Miyazaki", 3)]

def test_create_film(db_connection):
    db_connection.seed("seeds/films.sql")
    repository = FilmRepository(db_connection)

    repository.create(Film("Amelie", 2001, "Jean-Pierre Jeunet"))
    
    films = repository.all()

    assert films[-1] == Film("Amelie", 2001, "Jean-Pierre Jeunet", 4)
