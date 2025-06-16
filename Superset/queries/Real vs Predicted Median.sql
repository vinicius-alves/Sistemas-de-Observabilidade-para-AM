with t0 as (
  select  DISTINCT t0.idproject, t0.name as project, timestamp, value, identity
  from mysql.mydb.project as t0 
  left join mongodb.mydb.featurevalue as t1 
  on t0.idtargetfeature = t1.idfeature
  left join mysql.mydb.projecttype  as t2 
  on t0.idprojecttype = t2.idprojecttype
  where t2.name = 'Regression'
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

, marcacao_ordem as (
  select *, 
    row_number() over (partition by project, timestamp order  by y_true) AS rn_true,
    row_number() over (partition by project, timestamp order  by y_pred) AS rn_pred,
    count(*) over (partition by project, timestamp) AS total
  from base_valores 
)

select project, timestamp, 
AVG(case when rn_true in ((total + 1) / 2,
        (total + 2) / 2) then y_true else null end ) AS y_true_median,
        
AVG(case when rn_pred in ((total + 1) / 2,
        (total + 2) / 2) then y_pred else null end ) AS y_pred_median        

from marcacao_ordem
group by 1,2
