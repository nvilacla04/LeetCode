# Write your MySQL query statement below
select E.name, B.bonus 
from Employee E
    LEFT join Bonus B on E.empId = B.empId
where B.bonus < 1000
    or B.bonus is NULL