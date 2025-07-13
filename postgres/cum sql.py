create table pediatrics.headcount (
department varchar(20),
head_count int
);

insert into pediatrics.headcount values('Administration', 1);
insert into pediatrics.headcount values('HR', 1);
insert into pediatrics.headcount values('PR', 1);
insert into pediatrics.headcount values('MARKETING', 2);
insert into pediatrics.headcount values('Sales', 2);

select department, CUME_DIST() over (order by head_count) cume_dist_val
  from pediatrics.headcount;