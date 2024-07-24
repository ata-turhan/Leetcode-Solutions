with category_footages as (
    select item_type, sum(square_footage) as total_footage, count(*) as total_count from inventory group by item_type
)
select item_type,( (500000 DIV total_footage) * total_count) as item_count from category_footages where item_type = "prime_eligible"
union
select item_type, ( (500000 % (select total_footage from category_footages where item_type = "prime_eligible") DIV total_footage   ) * total_count) as item_count from category_footages where item_type = "not_prime"
