with subjectfeatures_pair as (

  select * from (
    select *, count(*) over(partition by idmeasure) as n_features 
    from mysql.mydb.subjectfeature
  )
  where n_features = 2
)

, mark_nrow_feature as (
  select t1.*, t4.name as feature, t5.name as namespace, row_number() over(partition by idmeasure order by t4.name) as nrow_feature
  from subjectfeatures_pair t1
  inner join mysql.mydb.feature as t4
  on t1.idfeature = t4.idfeature
  left join mysql.mydb.featurenamespace  as t5
  on t4.idfeaturenamespace = t5.idfeaturenamespace
)

, mark_feature as (

  select idmeasure, 
  max(case when nrow_feature =1 then feature else null end) as feature_reference,
  max(case when nrow_feature =2 then feature else null end) as feature_compare,
  max(case when nrow_feature =1 then namespace else null end) as feature_reference_namespace,
  max(case when nrow_feature =2 then namespace else null end) as feature_compare_namespace
  from mark_nrow_feature
  group by idmeasure
)




,base as (

    SELECT  t1.name as measure,  date(parse_datetime(t2.value, 'yyyy-MM-dd HH:mm:ss')) as timestamp, 
    t3.feature_reference, t3.feature_compare, t3.feature_reference_namespace as namespace, t3.feature_compare_namespace, round(try_cast(t0.value as double),2) value
    FROM mysql.mydb.measurevalue as t0 
    inner join mysql.mydb.measure as t1
    on t0.idmeasure = t1.idmeasure
    inner join mysql.mydb.parameter  as t2 
    on t0.idrun = t2.idrun
    inner join mark_feature as t3 
    on t0.idmeasure = t3.idmeasure 


    where t1.name like '%Correlation%'
    and t2.name = 'start_current_date'


)

select * 
from base
order by   feature_reference, feature_compare, timestamp