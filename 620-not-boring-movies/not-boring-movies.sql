# Write your MySQL query statement below
select C.id, C.movie, C.description, C.rating
from Cinema C
where C.id % 2 <> 0
    and C.description <> 'boring'
order by C.rating DESC