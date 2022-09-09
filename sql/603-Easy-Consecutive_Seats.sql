# 603. Consecutive Available Seats - 'Easy' - 2022Q3:Amzn

# Strat: self join, then pick seats with number that are 1 num different from each other(adjacent seats) and are free. 
#The conditions themselves can be used for joining.


SELECT DISTINCT A.seat_id FROM Cinema A JOIN Cinema B
    ON ABS(A.seat_id - B.seat_id) = 1
    AND A.free = True AND B.free = True
ORDER BY A.seat_id;
