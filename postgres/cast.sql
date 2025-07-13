CREATE TABLE pediatrics.members (
  id serial PRIMARY KEY,
  first_name VARCHAR (50) NOT NULL,
  last_name VARCHAR (50) NOT NULL,
  gender SMALLINT NOT NULL -- 1: male, 2 female
);

INSERT INTO pediatrics.members (first_name, last_name, gender)
VALUES
  ('A', 'Doe', 2),
  ('B', 'Dave', 1),
  ('C', 'Lily', 1)
RETURNING *;

select * from pediatrics.members;
select 
cast(sum(case when gender=1 then 1 else 0 end) / nullif(sum(case when gender=2 then 1 else 0 end),0)
as double precision) as "ratio"
from pediatrics.members;

