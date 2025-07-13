select name, salary, round(sum(salary) over(), 2) avg_salary from pediatrics.customers;

create table pediatrics.bonus_jan (
employee_id int,
name varchar(20),
position varchar(40),
outlet int,
region char(10),
bonus float
)
drop table pediatrics.bonus_jan;
INSERT into pediatrics.bonus_jan 
values (1, 'Max', 'Manager', 123, 'south', 2305.45),
(2, 'Jane', 'cashier', 105, 'north', 2315.45),
(3, 'Kate', 'customer service specialist', 123, 'east', 2405.45),
(4, 'Andrew', 'Manager', 105, 'south', 1305.45),
(5, 'John', 'cashier', 123, 'south', 305.45),
(6, 'Sebastian', 'customer service specialist', 123, 'east', 5305.45),
(7, 'Diana', 'Manager', 105, 'west',4305.45),
(8, 'Sofia', 'customer service specialist', 105, 'north', 105.45);

select * from pediatrics.bonus_jan;

select employee_id, name, bonus, position, avg(bonus) over( partition by position) avg_bonus_position
from pediatrics.bonus_jan order by employee_id;

WITH avg_position AS (
    SELECT position, AVG(bonus) AS average_bonus_for_position
    FROM pediatrics.bonus_jan
    GROUP BY position)
SELECT b.employee_id, b.name, b.position, b.bonus, ap.average_bonus_for_position
FROM pediatrics.bonus_jan b
inner JOIN avg_position ap
ON b.position = ap.position;


select employee_id, name, bonus, position, avg(bonus) over( partition by position) avg_bonus_position,
avg(bonus) over(partition by region) avg_bonus_region
from pediatrics.bonus_jan order by employee_id;

WITH avg_position AS (
    SELECT position, AVG(bonus) AS average_bonus_for_position
    FROM pediatrics.bonus_jan
    GROUP BY position),
	avg_region AS (
    SELECT region, AVG(bonus) AS average_bonus_for_region
    FROM pediatrics.bonus_jan
    GROUP BY region)
SELECT b.employee_id, b.name, b.position, b.bonus, ap.average_bonus_for_position, ar.average_bonus_for_region
FROM pediatrics.bonus_jan b
inner JOIN avg_position ap
ON b.position = ap.position
inner join avg_region ar
on b.region = ar.region;

-- select employee_id, name, bonus, position, outlet, 

with avg_per_outlet as (select outlet, avg(bonus)as average_bonus_for_outlet
from pediatrics.bonus_jan group by outlet)
select a.employee_id, a.name, a.bonus, a.outlet, b.average_bonus_for_outlet from pediatrics.bonus_jan a inner join avg_per_outlet as b 
on a.outlet = b.outlet;


with avg_bonus as (
select outlet, avg(bonus) as avg_bonus_for_outlet from pediatrics.bonus_jan group by outlet
),
min_avg_bonus as (
select min(avg_bonus_for_outlet) as min_avg_bonus_for_outlet from avg_bonus
),
max_avg_bonus as (
select max(avg_bonus_for_outlet) as max_avg_bonus_for_outlet from avg_bonus
)
select a.outlet, a.avg_bonus_for_outlet, b.min_avg_bonus_for_outlet, c.max_avg_bonus_for_outlet from avg_bonus a, min_avg_bonus b, max_avg_bonus c; 

WITH recursive RecursiveMonths AS (
    SELECT
        1 AS MonthNumber,
        to_char(CAST('2024-01-01' AS DATE), 'MM') AS MonthName

    UNION ALL

    SELECT
        MonthNumber + 1,
        to_char(DATEADD(MONTH, MonthNumber, '2024-01-01'), 'MM')
    FROM RecursiveMonths
    WHERE MonthNumber < 12
)
SELECT * FROM RecursiveMonths;

select datename(month, '2024-01-01');

select * from pediatrics.customers;
with avg_salary as 
(select avg(salary) as average_salary from pediatrics.customers)
select a.id, a.name, a.salary from pediatrics.customers a, avg_salary b where a.salary > b.average_salary;