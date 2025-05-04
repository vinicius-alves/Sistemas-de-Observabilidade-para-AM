 select  t1.idmodel,
  max(t2.name) as modelname,
  max(t2.version) as version,
  min(timestamp) as first_prediction,  
  max(timestamp) as last_prediction,
  max(t3.name) as projectname,
  count(*) as qtt_predicitons
  from mysql.mydb.prediction t0
  left join mysql.mydb.run t1
  on t0.idrun = t1.idrun
  left join mysql.mydb.model as t2
  on t1.idmodel = t2.idmodel
  left join mysql.mydb.project as t3 
  on t1.idproject = t3.idproject
  group by 1