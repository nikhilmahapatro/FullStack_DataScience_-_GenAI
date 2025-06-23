SELECT * FROM dataset_1 d 

SELECT weather, temperature FROM dataset_1 d 

SELECT * FROM dataset_1 d LIMIT 10

SELECT DISTINCT d.passanger FROM dataset_1 d 

SELECT * FROM dataset_1 d WHERE destination= 'Home'

SELECT * FROM dataset_1 d ORDER BY coupon 

SELECT destination AS Destination FROM dataset_1 d   

SELECT occupation FROM dataset_1 d GROUP BY occupation 

SELECT weather, AVG(temperature) AS avg_temp FROM dataset_1 GROUP BY weather 

SELECT weather ,COUNT(DISTINCT temperature) AS count_distinct_temp FROM dataset_1 GROUP BY weather

SELECT weather ,SUM(temperature) AS sum_temp FROM dataset_1 GROUP BY weather

SELECT weather ,MIN(temperature) AS min_temp FROM dataset_1 GROUP BY weather

SELECT weather ,MAX(temperature) AS max_temp FROM dataset_1 GROUP BY weather

SELECT occupation FROM dataset_1 GROUP BY occupation HAVING occupation='Student'












