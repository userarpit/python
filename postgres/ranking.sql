select * from pediatrics.customers;

select
    name,
    salary,
    cume_dist() over (
        order by salary
    )
from pediatrics.customers;

create table pediatrics.dense_rank_demos (v varchar);
insert into
pediatrics.dense_rank_demos (v)
values
('A'),
('B'),
('B'),
('C'),
('D'),
('D'),
('E');

select * from pediatrics.dense_rank_demos;
select
    v,
    dense_rank() over (
        order by v
    ) as dense_rank
from pediatrics.dense_rank_demos;

select * from (
    select
        v,
        dense_rank() over (
            order by v
        ) as dense_rank,
        rank() over (
            order by v
        ) as rank
    from pediatrics.dense_rank_demos
)
where rank = 2;

create table pediatrics.t (
    col int not null
);

insert into pediatrics.t (col)
values (1), (2), (3), (4), (5), (6), (7), (8), (9), (10);

select * from pediatrics.t;

select
    col,
    ntile(4) over (
        order by col
    ) as col_group
from pediatrics.t;

select
    name,
    salary,
    percentile_rank
from (
    select
        name,
        salary,
        percent_rank() over (
            -- PARTITION BY e.department_id
            order by salary
        )::float
        as percentile_rank
    from pediatrics.customers
);

select * from pediatrics.customers;


select
    name,
    salary,
    percent_rank() over (
        -- PARTITION BY e.department_id
        order by salary
    )::float
    as percentile_rank,
    row_number() over (
        order by salary
    ) as row_num
from pediatrics.customers;
