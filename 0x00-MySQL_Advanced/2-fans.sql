-- Task 2. Best band ever!
-- Ranks country origins of bands and ordered by number of fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;