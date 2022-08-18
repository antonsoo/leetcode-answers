# 175. Combine Two Tables - Easy - Companies:Adobe/Amzn
 # left join will put in city, state as null when firstName, lastName are not present for
    #those entries in city or state
SELECT firstName, lastName, city, state
FROM Person AS p LEFT JOIN Address AS a
    ON p.personID = a.personID;
    
