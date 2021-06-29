DROP DATABASE IF EXISTS books_db;
CREATE DATABASE books_db;
USE books_db;

DROP TABLE IF EXISTS books_db.authors;
CREATE TABLE authors (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    fname VARCHAR(250) DEFAULT NULL,
    lname VARCHAR(250) NOT NULL,
    birth_year SMALLINT(4) DEFAULT NULL,
    death_year SMALLINT(4) DEFAULT NULL,
    INDEX(lname(10)),
	PRIMARY KEY (id)
) DEFAULT CHARSET=utf8;

-- DROP TABLE IF EXISTS books_db.books;
CREATE TABLE books (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    author_id INT UNSIGNED NOT NULL,
    book_name VARCHAR(250) NOT NULL,
    pub_year SMALLINT(4) UNSIGNED DEFAULT NULL,
    INDEX(book_name(10)),
	PRIMARY KEY (id),
	FOREIGN KEY (author_id) REFERENCES authors (id)
) DEFAULT CHARSET=utf8;


INSERT INTO authors(fname,lname,birth_year,death_year) VALUES
    ('Kurt'   , 'Vonnegut', '1922','2007'),
    ('Douglas', 'Adams'   , '1952','2001'),
    ('Charles', 'Dodgson' , '1832','1898')
;

INSERT INTO books(author_id, book_name,pub_year) VALUES
    (1, 'The Sirens of Titan', 1959),
    (1, 'Mother Night', 1961),
    (1, 'Cat\'s Cradle', 1963), # note: the single quote inside string should be escaped!
    (1, 'God Bless You', 1965),
    (1, 'Slaughterhouse', 1969),
    (1, 'Breakfast of Champions', 1973),
    (2, "The Hitchhiker's Guide to the Galaxy", 1979),
    (2, 'The Restaurant at the End of the Universe', 1980),
    (2, 'Life', 1982),
    (2, 'So Long', 1984),
    (2, 'Young Zaphod Plays It Safe', 1986),
    (2, "Dirk Gently's Holistic Detective Agency", 1987),  #note: or we can use double quotes for string delimiter
    (2, 'The Long Dark Tea', 1988),
    (2, 'Last Chance to See', 1990),
    (2, 'Mostly Harmless', 1992),
    (3, "Alice's Adventures in Wonderland", 1865),
    (3, "Through the Looking-Glass, and What Alice Found There", 1871),
    (3, "Rhyme? And Reason?",NULL),
    (3, "A Tangled Tale",NULL),
    (3, "Pillow Problems",NULL),
    (3, "La Guida di Bragia, a Ballad Opera for the Marionette Theatre",1950),
    (3, "Sylvie and Bruno",NULL),
    (3, "Sylvie and Bruno Concluded",NULL),
    (3, "Three Sunsets and Other Poems", 1898),
    (3, "The Hunting of the Snark", 1876),
    (3, "What the Tortoise Said to Achilles", 1895),
    (3, "A Syllabus of Plane Algebraic Geometry", 1860),
    (3, "The Fifth Book of Euclid Treated Algebraically", 1858),
    (3, "An Elementary Treatise on Determinants, With Their Application to Simultaneous Linear Equations and Algebraic Equations",NULL),
    (3, "Euclid and his Modern Rivals",1879),
    (3, "Symbolic Logic Part I",NULL),
    (3, "Symbolic Logic Part II",NULL),
    (3, "The Alphabet Cipher",1868),
    (3, "The Game of Logic", 1887),
    (3, "Curiosa Mathematica I", 1888),
    (3, "Curiosa Mathematica II", 1892);

