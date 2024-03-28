select min(round(power(power((p1.x-p2.x), 2) + power((p1.y-p2.y), 2), 0.5), 2)) as shortest 
 from point2d as p1 join point2d as p2 on p1.x != p2.x or p1.y != p2.y