SELECT MOVIESTAR.NAME
FROM MOVIESTAR
INNER JOIN STARSIN
ON MOVIESTAR.NAME = STARSIN.STARNAME
WHERE MOVIESTAR.GENDER = 'M' AND STARSIN.MOVIETITLE = 'Terms of Endearment';

SELECT STARSIN.STARNAME
FROM STARSIN
INNER JOIN MOVIE
ON MOVIE.TITLE = STARSIN.MOVIETITLE
WHERE STARSIN.MOVIEYEAR = 1995 AND MOVIE.STUDIONAME = 'MGM';

ALTER TABLE STUDIO
ADD COLUMN PRESIDENT VARCHAR(255);

UPDATE STUDIO
SET PRESIDENT = 'Bill Clinton'
WHERE NAME = 'MGM';

SELECT PRESIDENT
FROM STUDIO
WHERE NAME = 'MGM';

SELECT TITLE
FROM MOVIE
WHERE LENGTH > (SELECT LENGTH
				FROM MOVIE
				WHERE TITLE = 'Gone With the Wind');

SELECT NETWORTH
FROM MOVIEEXEC
WHERE NETWORTH > (SELECT NETWORTH
				  FROM MOVIEEXEC
				  WHERE NAME = 'Merv Griffin');