CREATE TABLE regions (
    id INT,
    name VARCHAR(512),
    countryid VARCHAR(512)
);

INSERT INTO regions (id, name, countryid) VALUES
    (1, 'Moscow region', 1),
    (2, 'Lviv region', 3),
    (3, 'Styria', 4),
    (4, 'Tyrol', 4),
    (5, 'Bavaria', 5),
    (6, 'Berlin', 5),
    (7, 'Kyiv region', 3),
    (8, 'Almaty region', 2),
    (9, 'Nur-Sultan region', 2),
    (10, 'Saint Petersburg region', 1);