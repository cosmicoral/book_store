DROP TABLE IF EXISTS films;

CREATE TABLE films(
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    director text
);

INSERT INTO films (title, release_year, director) VALUES
('In the Mood for Love', 2000, 'Wong Kar-wai'),
('Chungking Express', 1994, 'Wong Kar-wai'),
('Spirited Away', 2001, 'Hayao Miyazaki');