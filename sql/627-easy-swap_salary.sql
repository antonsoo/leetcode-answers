# 627. Swap Salary - Easy - 2021:Amzn/Apple
UPDATE Salary # table name
SET sex = 
    CASE sex 
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
    

# second way: pythonic-like, 
#if cond1 is met then set to param1, else set to param2
#　update salary set sex = IF (sex = "m", "f", "m");
