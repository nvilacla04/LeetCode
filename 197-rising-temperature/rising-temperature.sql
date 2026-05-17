# Write your MySQL query statement below
select w2.id
from weather w1, weather w2
where w1.temperature < w2.temperature
and ADDDATE(W1.RecordDate, 1) = W2.RecordDate