# Write your MySQL query statement below
select e1.name as Employee 
from Employee as e1
inner join Employee as e2
on e1.ManagerId = e2.Id
where e1.salary > e2.salary