CREATE TABLE trips (
    id INT,
    company	INT,
    plane VARCHAR(512),
    town_from VARCHAR(512),
    town_to	VARCHAR(512),
    time_out DATETIME,
    time_in	DATETIME
);

INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1100, 4, 'Boeing', 'Rostov', 'Paris', '1900-01-01T14:30:00.000Z', '1900-01-01T17:50:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1101, 4, 'Boeing', 'Paris', 'Rostov', '1900-01-01T08:12:00.000Z', '1900-01-01T11:45:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1123, 3, 'TU-154', 'Rostov', 'Vladivostok', '1900-01-01T16:20:00.000Z', '1900-01-02T03:40:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1124, 3, 'TU-154', 'Vladivostok', 'Rostov', '1900-01-01T09:00:00.000Z', '1900-01-01T19:50:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1145, 2, 'IL-86', 'Moscow', 'Rostov', '1900-01-01T09:35:00.000Z', '1900-01-01T11:23:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1146, 2, 'IL-86', 'Rostov', 'Moscow', '1900-01-01T17:55:00.000Z', '1900-01-01T20:01:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1181, 1, 'TU-134', 'Rostov', 'Moscow', '1900-01-01T06:12:00.000Z', '1900-01-01T08:01:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1182, 1, 'TU-134', 'Moscow', 'Rostov', '1900-01-01T12:35:00.000Z', '1900-01-01T14:30:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1187, 1, 'TU-134', 'Rostov', 'Moscow', '1900-01-01T15:42:00.000Z', '1900-01-01T17:39:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1188, 1, 'TU-134', 'Moscow', 'Rostov', '1900-01-01T22:50:00.000Z', '1900-01-02T00:48:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1195, 1, 'TU-154', 'Rostov', 'Moscow', '1900-01-01T23:30:00.000Z', '1900-01-02T01:11:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (1196, 1, 'TU-154', 'Moscow', 'Rostov', '1900-01-01T04:00:00.000Z', '1900-01-01T05:45:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7771, 5, 'Boeing', 'London', 'Singapore', '1900-01-01T01:00:00.000Z', '1900-01-01T11:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7772, 5, 'Boeing', 'Singapore', 'London', '1900-01-01T12:00:00.000Z', '1900-01-02T02:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7773, 5, 'Boeing', 'London', 'Singapore', '1900-01-01T03:00:00.000Z', '1900-01-01T13:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7774, 5, 'Boeing', 'Singapore', 'London', '1900-01-01T14:00:00.000Z', '1900-01-02T06:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7775, 5, 'Boeing', 'London', 'Singapore', '1900-01-01T09:00:00.000Z', '1900-01-01T20:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7776, 5, 'Boeing', 'Singapore', 'London', '1900-01-01T18:00:00.000Z', '1900-01-02T08:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7777, 5, 'Boeing', 'London', 'Singapore', '1900-01-01T18:00:00.000Z', '1900-01-02T06:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (7778, 5, 'Boeing', 'Singapore', 'London', '1900-01-01T22:00:00.000Z', '1900-01-02T12:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (8881, 5, 'Boeing', 'London', 'Paris', '1900-01-01T03:00:00.000Z', '1900-01-01T04:00:00.000Z');
INSERT INTO trips (id, company, plane, town_from, town_to, time_out, time_in) VALUES (8882, 5, 'Boeing', 'Paris', 'London', '1900-01-01T22:00:00.000Z', '1900-01-01T23:00:00.000Z');