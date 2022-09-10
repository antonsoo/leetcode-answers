# 610. Triangle Judgement - Easy - 2022: FB

SELECT x, y, z,  
    CASE 
        WHEN x+y>z AND z+y>x AND x+z>y THEN "Yes"
        ELSE "No"
    END AS "triangle"
FROM Triangle;
