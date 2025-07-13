create table pediatrics.employees (
    name varchar(20),
    hire_date date
);

insert into pediatrics.employees values ('Arpit', '2007-06-18');
insert into pediatrics.employees values ('Ankit', '2008-04-20');
insert into pediatrics.employees values ('Basmati', '2009-11-23');
insert into pediatrics.employees values ('Jackson', '2003-09-05');
insert into pediatrics.employees values ('Maria', '2004-01-07');
insert into pediatrics.employees values ('Jane', '2000-02-19');
insert into pediatrics.employees values ('tkinter', '1997-07-11');

select * from pediatrics.employees;
truncate pediatrics.employees;

select
    name,
    hire_date,
    lead(hire_date) over (
        order by hire_date
    ) as next_hire_date
from
    pediatrics.employees;
