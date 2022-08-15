# 1484. Group Sold Products By The Date - Easy - 2022Q2:Adobe
SELECT sell_date, 
    COUNT(DISTINCT(product)) AS num_sold, 
    GROUP_CONCAT(DISTINCT(product) ORDER BY product) AS products
FROM Activities
GROUP BY sell_date;
