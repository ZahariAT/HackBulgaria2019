SELECT AVG(speed) AS AVGspeed
FROM pc;

SELECT AVG(laptop.screen) AS AVGscreen, product.maker
FROM laptop
JOIN product
ON product.model = laptop.model
GROUP BY product.maker;

SELECT AVG(speed) AS AVGspeed
FROM laptop
WHERE price > 1000;

SELECT AVG(price) AS AVGprice, hd
FROM pc
GROUP BY hd;

SELECT AVG(price) AS AVGprice
FROM pc
WHERE speed > 500;

SELECT AVG(pc.price) AS AVGprice, product.maker
FROM pc
JOIN product
ON product.model = pc.model
WHERE product.maker = 'A';

SELECT (AVG(pc.price) + AVG(laptop.price))/2 AS AVGprice
FROM product
LEFT OUTER JOIN laptop, pc -- OR INNER JOIN --
ON product.model = laptop.model OR product.model = pc.model
WHERE product.maker = 'B';

SELECT COUNT(model) AS COUNTmodel, maker
FROM product
GROUP BY maker
HAVING COUNT(model) >= 3;

SELECT product.maker
FROM product
JOIN pc
ON pc.model = product.model
WHERE pc.price = (SELECT MAX(price)
				  FROM pc);

SELECT AVG(pc.hd) AS AVGhd
FROM pc
JOIN product
ON product.model = pc.model
WHERE product.maker IN (SELECT maker
						FROM product
						WHERE type = 'Printer'
						GROUP BY maker);