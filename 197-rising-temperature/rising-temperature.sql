# Write your MySQL query statement below
select today.id 
from Weather today
    join Weather ystd
    on DATEDIFF(today.recordDate, ystd.recordDate) = 1
where today.temperature > ystd.temperature 