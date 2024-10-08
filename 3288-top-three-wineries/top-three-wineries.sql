with total_points as (
    select country, winery, sum(points) as sum_points from wineries group by country, winery
),
rankings as (
    select country, winery, sum_points, rank() over (partition by country order by sum_points desc, winery asc) as ranks from total_points
)
select r1.country, 
concat(r1.winery, " (", r1.sum_points, ")") as top_winery,
ifnull(concat(r2.winery, " (", r2.sum_points, ")"), "No second winery") as second_winery,
ifnull(concat(r3.winery, " (", r3.sum_points, ")"), "No third winery") as third_winery


from rankings as r1 left join rankings as r2 on r1.country = r2.country and r1.ranks = 1 and r2.ranks = 2 left join rankings as r3 on r1.country = r3.country and r1.ranks = 1 and r3.ranks = 3 where r1.ranks = 1
