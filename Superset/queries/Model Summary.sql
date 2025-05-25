with gen_summary as (

     select  t1.idmodel,
    max(t2.name) as modelname,
    max(t2.version) as version,
    min(timestamp) as first_prediction,  
    max(timestamp) as last_prediction,
    max(t3.name) as project,
    count(*) as qtt_predictions
    from mysql.mydb.prediction t0
    left join mysql.mydb.run t1
    on t0.idrun = t1.idrun
    left join mysql.mydb.model as t2
    on t1.idmodel = t2.idmodel
    left join mysql.mydb.project as t3 
    on t1.idproject = t3.idproject
    group by 1
)
    
, filter_training_run as (

  select * from mysql.mydb.tasktype
  where type = 'Training'

)


, base as (

  select * from (
    select t0.idrun, t0.idmodel,  
    row_number() over(partition by idmodel order by t0.idrun desc) as nrow
    from mysql.mydb.run as t0 
    left join mysql.mydb.task as t1 
    on t0.idtask = t1.idtask
    inner join filter_training_run as t2 
    on t1.idtasktype = t2.idtasktype
  ) where nrow = 1
)
, measures_models as (
    select t0.idmodel, t1.name as measure ,t1.value
    from base as t0 
    left join mysql.mydb.measure as t1
    on t0.idrun = t1.idrun
    order by t0.idmodel, measure
)

select t0.*, t1.measure, t1.value from gen_summary as t0 
left join measures_models as t1 
on t0.idmodel = t1.idmodel

order by t0.idmodel, measure