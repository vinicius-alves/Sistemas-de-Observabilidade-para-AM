select distinct t0.name as project, t1.idmodel, t5.name as feature, 1 as flag
  from mysql.mydb.project as t0
  inner join mysql.mydb.run as t1 
  on t0.idproject = t1.idproject 
  inner join mysql.mydb.dataset as t3 
  on t1.idDataset = t3.idDataset
  inner join mysql.mydb.featuredataset as t4 
  on t3.iddataset = t4.iddataset
  inner join mysql.mydb.feature as t5 
  on t4.idfeature = t5.idfeature
  where t1.idmodel is not null 
  and t4.idfeature != t0.idtargetfeature