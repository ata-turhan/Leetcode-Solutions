# Write your MySQL query statement below
select concat(t1.topping_name, ",", t2.topping_name , ",", t3.topping_name) as pizza,
(t1.cost + t2.cost + t3.cost) as total_cost
 from toppings as t1 join toppings as t2 
on t1.topping_name < t2.topping_name join toppings as t3 on t2.topping_name < t3.topping_name 
order by total_cost desc, pizza asc;  