-- list all the cities of california
-- from database
SELECT cities.id, cities.name  
FROM cities  
WHERE state_id IN (SELECT id FROM states WHERE name = 'California');

