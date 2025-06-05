with base as (

    SELECT  t1.name as measure,  date(parse_datetime(t2.value, 'yyyy-MM-dd HH:mm:ss')) as timestamp, 
    t4.name as feature, t5.name as namespace, cast(t0.value as double) value
    FROM mysql.mydb.measurevalue as t0 
    inner join mysql.mydb.measure as t1
    on t0.idmeasure = t1.idmeasure
    inner join mysql.mydb.parameter  as t2 
    on t0.idrun = t2.idrun
    inner join mysql.mydb.subjectfeature as t3 
    on t0.idmeasure = t3.idmeasure
    inner join mysql.mydb.feature as t4
    on t3.idfeature = t4.idfeature
    left join mysql.mydb.featurenamespace  as t5
    on t4.idfeaturenamespace = t5.idfeaturenamespace


    where t1.name like '%Jensen-Shannon%'
    and t2.name = 'start_current_date'


)

select *, max(value) over(partition by namespace,feature) as max_value 
from base
order by  max_value desc, feature, timestamp