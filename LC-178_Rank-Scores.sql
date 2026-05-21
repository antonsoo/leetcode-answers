# Problem: 178. Rank Scores
# Solution: https://leetcode.com/problems/rank-scores/solutions/7045886/easy-solution-by-nramana97-8g2h/

SELECT S.score, COUNT(S2.SCORE) as `rank` FROM SCORES S,
    (SELECT DISTINCT SCORE FROM SCORES) S2
WHERE S.SCORE <= S2.SCORE 
GROUP BY S.ID 
ORDER BY S.SCORE DESC;
