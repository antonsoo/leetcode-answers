# 1693. Daily Leads and Partners - Easy - 2022Q3: No companies
# Problem: Group each company ('make_name') by the date_id
#and then count the number of unique leads and the number of unique
#partners for each date (grouping by each day and each company)

SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
    FROM DailySales
GROUP BY date_id, make_name # the order on this line doesn't matter
# also the order of the data doesn't matter
