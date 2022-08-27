# 175. Combine Two Tables - Easy - Companies:Adobe/Amzn
 # left join will put in city, state as null when firstName, lastName are not present for those entries in city or state
 # that's what the question asked us to do in the descrp. btw
SELECT firstName, lastName, city, state
FROM Person NATURAL LEFT JOIN Address;
#FROM Person AS p LEFT JOIN Address AS a;
#    ON p.personID = a.personID;
    
