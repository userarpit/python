select justify_days(interval '35 days');
select justify_hours(interval '101 hours');

create table PEDIATRICS.EVENT (
    ID serial primary key,
    EVENT_NAME varchar(255) not null,
    DURATION interval not null
);
truncate table PEDIATRICS.EVENT;
set intervalstyle = 'iso_8601';
insert into PEDIATRICS.EVENT (EVENT_NAME, DURATION)
values ('pgConf', '1 hour 30 minutes'),
('pgDAY', '2 days 5 hours')

returning *;


select
    EVENT_NAME,
    DURATION,
    extract(day from DURATION) as DAYS,
    extract(hour from DURATION) as HOURS,
    extract(minute from DURATION) as MINUTES
from PEDIATRICS.EVENT;

select * from PEDIATRICS.EVENT
where DURATION > interval '1 day';

with TOTAL_DURATION as (
    select sum(DURATION) as TOTAL from PEDIATRICS.EVENT
)

select
    TD.TOTAL,
    extract(day from TD.TOTAL) as DAYS,
    extract(hour from TD.TOTAL) as HOURS,
    extract(minute from TD.TOTAL) as MINUTES

from TOTAL_DURATION as TD;
