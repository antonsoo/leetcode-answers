# 1084. Sales Analysis III - Ez - 2020:Amzn

# note: we're finding products that were *only* sold between those dates, so not products that were sold both on those dates and not on those dates. #WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31' doesn't work cuz of the reason I explain above.
# inner join since we don't care about prducts that weren't sold
# lesson learned: MIN() and MAX() work with dates perfectly fine.

SELECT product_id, product_name
FROM Product P NATURAL JOIN Sales S
GROUP BY product_id
HAVING MIN(sale_date)>='2019-01-01' AND MAX(sale_date)<='2019-03-31' 
