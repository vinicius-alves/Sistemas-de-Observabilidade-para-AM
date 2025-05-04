with t0 as (
  select  DISTINCT name as projectname, timestamp, value  
  from mysql.mydb.project as t0 
  left join mongodb.mydb.featurevalue as t1 
  on t0.idtargetfeature = t1.idfeature
)

, t1 as (
select DISTINCT (timestamp - INTERVAL '3' HOUR) as timestamp, value
from mysql.mydb.prediction
)

select projectname , t1.timestamp, cast(t0.value as double) as y_true, cast(t1.value as double) as y_pred from t1 
inner join t0 
on t0.timestamp = t1.timestamp