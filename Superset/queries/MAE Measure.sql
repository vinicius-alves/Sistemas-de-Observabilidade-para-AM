

with stard_date_parameter as (

  select * from mysql.mydb.parameter 
    where name = 'start_date'

)

, filter_task_type as (

  select * from mysql.mydb.tasktype
  where type = 'Prediction'

)

, base as (
 
  select t0.idrun, 
  date(parse_datetime(t4.value, 'yyyy-MM-dd HH:mm:ss')) as timestamp, 
  t3.name as project  
  from mysql.mydb.run as t0 
  left join mysql.mydb.task as t1 
  on t0.idtask = t1.idtask
  inner join filter_task_type as t2 
  on t1.idtasktype = t2.idtasktype 
  left join mysql.mydb.project as t3 
  on t0.idproject = t3.idproject
  inner join stard_date_parameter as t4
  on t0.idRun = t4.idRun   
     
 
)

select timestamp, t0.project, t2.name as measure , cast(t1.value as double) as value
from base as t0 
inner join mysql.mydb.measurevalue as t1
on t0.idrun = t1.idrun
inner join mysql.mydb.measure as t2
on t1.idmeasure = t2.idmeasure
where t2.name = 'MAE' 
order by timestamp, measure
