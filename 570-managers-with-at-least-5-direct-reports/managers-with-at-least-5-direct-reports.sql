# Write your MySQL query statement below
select E.name 
from Employee E
    Left join Employee E2
        on E.id = E2.managerId
group by E.id, E.name
having count(E2.id) >= 5