SELECT CONCAT(t1.topping_name, ',', t2.topping_name, ',', t3.topping_name) AS pizza,
       (t1.cost + t2.cost + t3.cost) AS total_cost
FROM toppings AS t1
JOIN toppings AS t2 ON t1.topping_name < t2.topping_name
JOIN toppings AS t3 ON t2.topping_name < t3.topping_name
ORDER BY total_cost DESC, pizza ASC;
