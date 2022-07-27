# 595. Big Countries - Easy - 2022Q2: Googl/Amzn/etc
# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
