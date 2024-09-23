CREATE TABLE cities (
    id INT,
    name VARCHAR(512),
    regionid INT,
    population INT
);

INSERT INTO cities (id, name, regionid, population) VALUES
    (1, 'Moscow', 1, 13000000),
    (2, 'Saint Petersburg', 10, 5500000),
    (3, 'Graz', 3, 300000),
    (4, 'Innsbruck', 4, 132000),
    (5, 'Munich', 5, 1470000),
    (6, 'Berlin', 6, 3645000),
    (7, 'Kyiv', 7, 2884000),
    (8, 'Almaty', 8, 1850000),
    (9, 'Nur-Sultan', 9, 1100000),
    (10, 'Lviv', 2, 721301),
    (11, 'Salzburg', 4, 154211),
    (12, 'Nuremberg', 5, 518365),
    (13, 'Frankfurt', 5, 753056),
    (14, 'Hamburg', 6, 1841000),
    (15, 'Dresden', 6, 554649),
    (16, 'Leipzig', 6, 587857),
    (17, 'Stuttgart', 5, 634830),
    (18, 'Dortmund', 6, 588462),
    (19, 'Vienna', 4, 1897000),
    (20, 'Krakow', 2, 766683);