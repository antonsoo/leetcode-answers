# 619. Biggest Single Number
# Solution from: https://leetcode.com/problems/biggest-single-number/solutions/7704920/sql-solution-by-pranav_decodes-isbp/

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;
