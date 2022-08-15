# 1527. Patients With a Condition - easy - no companies
# Notice, we want to match DIAB1.... whether it's in the middle or the end or the start. 
# We don't want to match anything like ASDFGDIAB1
# we do want to match something like DIAB104763SDFS473 or 'ASDF DIAB1'
SELECT * FROM Patients
WHERE conditions LIKE "% DIAB1%" 
OR conditions LIKE "DIAB1%";
