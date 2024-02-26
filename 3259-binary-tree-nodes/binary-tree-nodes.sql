# Write your MySQL query statement below
select N, 
(case
when
p is null
then
"Root"
when
n in (select p from tree)
then
"Inner"
else
"Leaf"
end)
as type
from tree
order by N;