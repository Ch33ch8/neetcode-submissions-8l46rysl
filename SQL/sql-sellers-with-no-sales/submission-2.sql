-- Write your query below
SELECT seller_name from seller
WHERE seller_id NOT IN (select seller_id from orders WHERE sale_date between '2020-1-1' and '2020-12-31')
GROUP BY seller_name