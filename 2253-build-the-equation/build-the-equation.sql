with terms_vertical as (
    select power,
case
when power = 0 then
if(substr(factor, 1, 1) = "-", factor, concat("+", factor))
when power = 1 then
if(substr(factor, 1, 1) = "-", concat(factor, "X"), concat("+", factor, "X"))
else
if(substr(factor, 1, 1) = "-", concat(factor, "X", "^", power), concat("+", factor, "X", "^", power))
end
as term
from terms
)
select CONCAT(group_concat(term order by power desc  SEPARATOR ""), "=0") as equation from terms_vertical
