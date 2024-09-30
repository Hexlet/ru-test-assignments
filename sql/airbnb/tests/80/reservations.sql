CREATE TABLE reservations (
    id INT,
    user_id INT,
    room_id INT,
    start_date DATETIME,
    end_date DATETIME,
    price INT,
    total INT
);

INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (1, 1, 1, '2018-11-13T12:00:00.000Z', '2018-11-15T12:00:00.000Z', 140, 280);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (2, 2, 1, '2018-10-09T12:00:00.000Z', '2018-10-12T12:00:00.000Z', 120, 360);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (3, 12, 1, '2018-12-29T12:00:00.000Z', '2019-01-07T12:00:00.000Z', 180, 1620);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (4, 13, 1, '2019-02-01T12:00:00.000Z', '2019-02-02T12:00:00.000Z', 145, 145);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (5, 17, 1, '2019-02-02T12:00:00.000Z', '2019-02-04T12:00:00.000Z', 149, 298);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (6, 14, 2, '2020-03-21T09:00:00.000Z', '2020-03-23T09:00:00.000Z', 225, 450);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (7, 19, 13, '2020-03-21T10:00:00.000Z', '2020-04-21T10:00:00.000Z', 89, 2679);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (8, 29, 16, '2019-06-14T10:00:00.000Z', '2019-06-24T10:00:00.000Z', 140, 1400);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (9, 32, 21, '2019-05-11T10:00:00.000Z', '2019-05-14T10:00:00.000Z', 270, 810);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (10, 13, 21, '2019-11-04T10:00:00.000Z', '2019-11-06T10:00:00.000Z', 280, 560);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (11, 9, 21, '2020-02-28T10:00:00.000Z', '2020-02-29T10:00:00.000Z', 290, 290);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (12, 7, 19, '2020-05-01T10:00:00.000Z', '2020-05-02T10:00:00.000Z', 99, 99);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (13, 15, 8, '2020-01-19T12:00:00.000Z', '2020-01-21T12:00:00.000Z', 78, 156);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (14, 13, 7, '2019-09-13T10:00:00.000Z', '2019-09-17T10:00:00.000Z', 60, 240);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (15, 12, 5, '2020-05-14T10:00:00.000Z', '2020-05-15T10:00:00.000Z', 80, 80);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (16, 10, 5, '2020-03-26T10:00:00.000Z', '2020-03-27T10:00:00.000Z', 80, 80);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (17, 11, 50, '2019-11-18T11:00:00.000Z', '2019-11-25T11:00:00.000Z', 80, 560);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (18, 27, 49, '2019-09-18T11:00:00.000Z', '2019-09-20T11:00:00.000Z', 110, 220);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (19, 28, 49, '2020-04-01T11:00:00.000Z', '2020-04-02T11:00:00.000Z', 115, 115);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (20, 1, 49, '2020-06-01T10:00:00.000Z', '2020-06-11T10:00:00.000Z', 115, 1150);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (21, 2, 48, '2019-11-07T10:00:00.000Z', '2019-11-10T10:00:00.000Z', 110, 330);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (22, 12, 32, '2020-01-14T13:00:00.000Z', '2020-01-18T13:00:00.000Z', 52, 208);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (23, 12, 32, '2019-09-17T13:00:00.000Z', '2019-09-18T13:00:00.000Z', 52, 52);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (24, 7, 19, '2020-01-08T13:00:00.000Z', '2020-01-11T13:00:00.000Z', 99, 297);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (25, 18, 19, '2019-11-01T10:00:00.000Z', '2019-11-16T10:00:00.000Z', 99, 1485);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (26, 21, 17, '2019-11-03T09:00:00.000Z', '2019-11-05T09:00:00.000Z', 215, 430);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (27, 31, 25, '2020-04-20T09:00:00.000Z', '2020-04-22T09:00:00.000Z', 120, 240);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (28, 21, 14, '2020-02-08T10:00:00.000Z', '2020-02-12T10:00:00.000Z', 85, 340);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (29, 21, 39, '2019-12-08T10:00:00.000Z', '2019-12-09T10:00:00.000Z', 150, 150);
INSERT INTO reservations (id, user_id, room_id, start_date, end_date, price, total) VALUES (30, 3, 38, '2020-03-20T10:00:00.000Z', '2020-03-23T10:00:00.000Z', 185, 555);