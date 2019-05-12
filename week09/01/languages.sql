DROP TABLE IF EXISTS Languages;

CREATE TABLE Languages(
    id INTEGER PRIMARY KEY,
    language VARCHAR(40) NOT NULL,
    answer VARCHAR(40) NOT NULL,
    answered BOOLEAN,
    guide TEXT
);

INSERT INTO Languages (id, language, answer, answered,guide)
VALUES (1, 'Python', 'google', 0, 'A folder named Python was created. Go there and fight with program.py!');

INSERT INTO Languages (id, language, answer, answered,guide)
VALUES (2,'Go','200 OK', 0,'A folder named Go was created. Go there and try to make Google Go run.'),
       (3,'Java','Object Oriented Programming', 0,'A folder named Java was created. Can you handle the class?'),
       (4,'Haskell','Lambda', 0,'Something pure has landed. Go to Haskell folder and see it!'),
       (5,'C#','NDI=', 0,'Do you see sharp? Go to the C# folder and check out.'),
       (6,'Ruby','https://www.ruby-lang.org/bg/', 0, 'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!'),
       (7,'C++','Header files', 0,'Here be dragons! It''s C++ time. Go to the C++ folder.'),
       (8,'JavaScript','Douglas Crockford', 0, 'NodeJS time. Go to JavaScript folder and Node your way!');

ALTER TABLE Languages
  ADD COLUMN rating INTEGER;

UPDATE Languages
   SET rating = 2
 WHERE id = 1 OR id = 3;

UPDATE Languages
   SET rating = 4
 WHERE id = 2 
    OR id = 4;

UPDATE Languages
   SET rating = 8
 WHERE id = 5 
    OR id = 6;

UPDATE Languages
   SET rating = 3
 WHERE rating = NULL;

UPDATE Languages
   SET answered = 1
 WHERE language = 'Python' 
    OR language = 'Go';

SELECT language
  FROM Languages
 WHERE answer = '200 OK' 
    OR answer = 'Lambda';