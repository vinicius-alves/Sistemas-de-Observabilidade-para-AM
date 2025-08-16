with features_project as (

  select distinct t0.name as project, t0.idtargetfeature, t4.idfeature
  from mysql.mydb.project as t0
  inner join mysql.mydb.run as t1 
  on t0.idproject = t1.idproject 
  inner join mysql.mydb.dataset as t3 
  on t1.idDataset = t3.idDataset
  inner join mysql.mydb.featuredataset as t4 
  on t3.iddataset = t4.iddataset

)

,detail_feature as (
  select t0.*, t1.name as feature, t2.name as featurenamespace 
  from features_project as t0 
  left join mysql.mydb.feature as t1 
  on t0.idfeature = t1.idfeature
  left join mysql.mydb.featurenamespace  as t2
  on t1.idfeaturenamespace = t2.idfeaturenamespace
  where t0.idtargetfeature != t1.idfeature
)

select t1.*, t0.value, t0.timestamp, t0.idEntity 
from mongodb.mydb.featurevalue as t0 
inner join detail_feature as t1 
on t0.idfeature = t1.idfeature
order by t1.featurenamespace, t1.feature