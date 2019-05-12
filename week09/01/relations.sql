SELECT moviestar.name
  FROM moviestar
       INNER JOIN starsin
               ON moviestar.name = starsin.starname
 WHERE moviestar.gender = 'M'
       AND starsin.movietitle = 'Terms of Endearment';

SELECT starsin.starname
  FROM starsin
       INNER JOIN movie
               ON movie.title = starsin.movietitle
 WHERE starsin.movieyear = 1995
   AND movie.studioname = 'MGM';

ALTER TABLE studio
  ADD COLUMN president VARCHAR(255);

UPDATE studio
   SET president = 'Bill Clinton'
 WHERE name = 'MGM';

SELECT president
  FROM studio
 WHERE name = 'MGM';

SELECT title
  FROM movie
 WHERE length > (SELECT length
                   FROM movie
                  WHERE title = 'Gone With the Wind');

SELECT networth
  FROM movieexec
 WHERE networth > (SELECT networth
                     FROM movieexec
                    WHERE name = 'Merv Griffin');