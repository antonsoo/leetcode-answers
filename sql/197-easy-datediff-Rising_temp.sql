# 197. Rising Temperature - "Easy" - 2022Q3:Adobe/Amzn
# You just have to know these functions.

# the first way, DATEDIFF(table1.ColName, table2.ColName) = 1 (there is a diff)
# you join the table with itself on that difference, so the only values that 
#show up are the dates that are different from one another. You can also add
#another difference to join on.
SELECT w1.id FROM weather w1 JOIN weather w2 
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
    AND w1.Temperature > w2.Temperature;
    
