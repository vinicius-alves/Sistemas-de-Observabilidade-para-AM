with t0 as (
  select  DISTINCT t0.idproject, t0.name as project, timestamp, value, identity
  from mysql.mydb.project as t0 
  left join mongodb.mydb.featurevalue as t1 
  on t0.idtargetfeature = t1.idfeature
  left join mysql.mydb.projecttype  as t2 
  on t0.idprojecttype = t2.idprojecttype
  where t2.name = 'Classification'
)

, t1 as (
select DISTINCT (timestamp - INTERVAL '3' HOUR) as timestamp, value, identity, t1.idproject
from mysql.mydb.prediction as t0 
left join mysql.mydb.run as t1 
on t0.idrun = t1.idrun
)
 

, base_valores as (

  select project , date(t1.timestamp) as timestamp, 
  cast(t0.value as double) as y_true, cast(t1.value as double) as y_pred
  from t1 inner join t0 
  on t0.timestamp = t1.timestamp
  and t0.identity = t1.identity
  and t0.idproject = t1.idproject 
)

select project, timestamp, sum(y_true) as y_true, sum(y_pred) as y_pred
from base_valores
group by 1,2
