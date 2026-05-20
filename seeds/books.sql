CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
);

TRUNCATE TABLE books;

INSERT INTO books (title, author_name)
VALUES ('The Gruffalo', 'Julia Donaldson');

INSERT INTO books (title, author_name)
VALUES ('Ada Twist, Scientist', 'Andrea Beaty');

INSERT INTO books (title, author_name)
VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');

INSERT INTO books (title, author_name)
VALUES ('Dragons in a Bag', 'Zetta Elliott');