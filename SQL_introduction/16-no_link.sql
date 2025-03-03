--  computes the score average of all records
-- result column name is average
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;