SELECT address
  FROM studio
 WHERE name = 'MGM';

SELECT birthdate
  FROM moviestar
 WHERE name = 'Kim Basinger';

SELECT name
  FROM movieexec
 WHERE networth > 10000000;

SELECT name
  FROM moviestar
 WHERE gender = 'M'
    OR address = 'Prefect Rd.';

INSERT INTO moviestar
VALUES      ('Zahari Baharov', 'Boulevard Vasil Levski', 'M', '1900-01-01');

DELETE FROM studio
 WHERE address LIKE '%5%';

UPDATE movie
   SET studioname = 'Fox'
 WHERE title LIKE '%Star%';  