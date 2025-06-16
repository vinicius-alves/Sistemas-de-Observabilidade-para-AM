with features_values as (
  SELECT DISTINCT t0.*, t1.name, t2.name as namespace
   from mongodb.mydb.featurevalue t0
  inner join mysql.mydb.feature t1 
  on t0.idfeature = t1.idfeature 
  inner join mysql.mydb.featurenamespace t2
  on t1.idfeaturenamespace = t2.idfeaturenamespace 
)

, features_values_num as (

    select * from features_values
    where   type  in ('int','float')
)

, rank_name as (

    select *, 
    row_number() over (partition by namespace order by  name) as rank
     from (select distinct name, namespace from features_values_num)
)


  select date_trunc('month', timestamp) as mes, format_datetime(timestamp, 'YYYY-MM') AS mes_formatado,
  timestamp, cast(t0.value as double) value, t0.name, t0.namespace, rank
  from features_values_num as t0 
  left join rank_name as t1 
  on t0.name = t1.name 
  and t0.namespace = t1.namespace
 