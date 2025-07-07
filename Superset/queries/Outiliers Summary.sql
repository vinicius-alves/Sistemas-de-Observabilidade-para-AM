with base as (

    SELECT  
    t3.identity, (t3.timestamp - INTERVAL '3' HOUR) as timestamp, case when cast(t0.value as double) = -1 then 1 else 0 end as outlier, t5.name as project 
    FROM mysql.mydb.measurevalue as t0 
    inner join mysql.mydb.measure as t1
    on t0.idmeasure = t1.idmeasure
    inner join mysql.mydb.parameter  as t2 
    on t0.idrun = t2.idrun
    inner join mysql.mydb.subjectentity  as t3 
    on t0.idmeasure = t3.idmeasure
    inner join mysql.mydb.run as t4 
    on t0.idrun = t4.idrun
    inner join mysql.mydb.project as t5 
    on t4.idproject = t5.idproject
    


    where t1.name = 'Outlier'
    and t2.name = 'start_current_date'


)

, marcacao_mes as (
  select *, date_trunc('month', timestamp) as month
  from base  
)

, summary as (

  select month, project, sum(outlier) as outliers,  count(*) as total from marcacao_mes
  group by month, project 
)

select *, round(outliers/cast( total as double),2) as percentage_outliers from summary