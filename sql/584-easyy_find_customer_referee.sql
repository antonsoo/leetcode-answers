# 584. Find Customer Referee - Very Easy - no companies
# note: you can't just write 'WHERE referee_id != 2' because it will 
# skip all the NULL numbers. So you have to add "or ... is NULL"
# note: '= NULL' doesn't work, it has to be 'is NULL'
# note: <> and != are the same.
SELECT name from Customer
WHERE referee_id != 2 or referee_id is NULL;
