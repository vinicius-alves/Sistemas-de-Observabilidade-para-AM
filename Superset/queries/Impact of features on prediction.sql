with contributions_base as (

  select idfeature, contribution, idprediction,  
  case when percent_contribution <0 then -percent_contribution else percent_contribution end as percent_contribution
  from (
    select   *, contribution/(sum(contribution) over (partition by idprediction)) as percent_contribution
    from mysql.mydb.predictionfeaturecontribution
  )
)

, prediction_contribution_agg as (  
  select idfeature, contribution, idprediction
  from contributions_base
  where percent_contribution >= 0.02
  
  union 
  
  select 
  null as idfeature, sum(contribution) as contribution, idprediction
  
  from contributions_base
  where percent_contribution < 0.02
  group by idprediction
)



SELECT   t4.name as project, (t2.timestamp - INTERVAL '3' HOUR)  as timestamp, t2.idEntity,
concat( case when t1.name = 'bias' then ' ' else '' end, coalesce(t1.name,'others')) as feature,t0.contribution
FROM prediction_contribution_agg as t0 
left join mysql.mydb.feature as t1 
on t0.idFeature = t1.idFeature
left join mysql.mydb.prediction  as t2 
on t0.idPrediction = t2.idPrediction
left join mysql.mydb.run as t3 
on t2.idRun = t3.idRun
left join mysql.mydb.project as t4 
on t3.idProject = t4.idProject
order by 1, 2,3,4