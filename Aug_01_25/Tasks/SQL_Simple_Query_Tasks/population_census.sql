<<<<<<< HEAD
SELECT SUM(c.population) AS Total_Population
FROM city c
JOIN country co ON c.countrycode = co.code
WHERE co.continent = 'Asia';

SELECT c.name AS City_Name
FROM city c
JOIN country co ON c.countrycode = co.code
WHERE co.continent = 'africa';

SELECT co.continent AS Continent_Name,
       ROUND(AVG(c.population)) AS Average_Population
FROM city c
JOIN country co ON c.countrycode = co.code
GROUP BY co.continent;

=======
SELECT SUM(c.population) AS Total_Population
FROM city c
JOIN country co ON c.countrycode = co.code
WHERE co.continent = 'Asia';

SELECT c.name AS City_Name
FROM city c
JOIN country co ON c.countrycode = co.code
WHERE co.continent = 'africa';

SELECT co.continent AS Continent_Name,
       ROUND(AVG(c.population)) AS Average_Population
FROM city c
JOIN country co ON c.countrycode = co.code
GROUP BY co.continent;

>>>>>>> a095286 (Save local changes before pull)
       