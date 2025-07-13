CREATE TABLE pediatrics.customers (
    id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    address CHAR(25),
    salary DECIMAL(18, 2),
    PRIMARY KEY (id)
);

INSERT INTO pediatrics.customers (id, name, age, address, salary)
VALUES (1, 'Ramesh', 32, 'Ahmedabad', 2000.00);
INSERT INTO pediatrics.customers (id, name, age, address, salary)
VALUES (2, 'Khilan', 25, 'Delhi', 1500.00);
INSERT INTO pediatrics.customers (id, name, age, address, salary)
VALUES (3, 'kaushik', 23, 'Kota', 2000.00);
INSERT INTO pediatrics.customers (id, name, age, address, salary)
VALUES (4, 'Chaitali', 25, 'Mumbai', 6500.00);
INSERT INTO pediatrics.customers (id, name, age, address, salary)
VALUES (5, 'Hardik', 27, 'Bhopal', 8500.00);
INSERT INTO pediatrics.customers (id, name, age, address, salary)
VALUES (6, 'Komal', 22, 'MP', 4500.00);

select name, salary,
case 
when salary < 1500 then 'Low'
when salary >= 1500 and salary <4000 then 'Medium'
when salary >= 4000 then 'High'
else 'no salary'
end as salary_staus 
from pediatrics.customers;


select  
sum(case when salary < 1500 then 1 else 0 end) as "Low",
sum(case when salary >= 1500 and salary < 4000 then 1 else 0 end) as "Medium",
sum(case when salary > 4000 then 1 else 0 end) as "High"
from pediatrics.customers;


select name, coalesce(address,name) from pediatrics.customers;


select * from pediatrics.customers;


