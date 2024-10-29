with sales_by_years as (
    select product_id, year(transaction_date) as year_val, sum(spend) as total_spend from user_transactions group by product_id, year_val
),
sales_by_cur_and_prev_years as (
    select year_val, product_id, total_spend as curr_year_spend, lag(total_spend, 1) over (partition by product_id order by year_val asc) as prev_year_spend from sales_by_years
)
select year_val as year, product_id, curr_year_spend, prev_year_spend,
round((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) as yoy_rate 
 from sales_by_cur_and_prev_years;