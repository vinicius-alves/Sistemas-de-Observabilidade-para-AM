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
    where   type  in ('str')
)

, detail as (
  select date_trunc('month', timestamp) as mes,  format_datetime(timestamp, 'YYYY-MM') AS mes_formatado,
   timestamp,   coalesce(value, 'missing') as value, name, namespace
  from features_values_num 
  
)

, sumario as (
  select mes, mes_formatado, value, name, namespace, count(*) as qt 
  from detail
  group by 1, 2, 3, 4, 5 
)

, calc_percent as (
  select *, cast(qt as double)/(sum(qt) over (partition by mes, name, namespace)) as qt_percent 
  from sumario
)


, treatment as (
  select mes, mes_formatado,  value, name, namespace, qt_percent from  calc_percent
  where qt_percent >= 0.05
  union all 
  
  select mes, mes_formatado, 'others' as value, name, namespace, sum(qt_percent) as qt_percent  from  calc_percent
  where qt_percent < 0.05
  group by mes, mes_formatado, name, namespace
)

, rank_name as (

    select *, 
    row_number() over (partition by namespace order by  name) as rank
     from (select distinct name, namespace from treatment)
)

select t0.*, t1.rank from treatment as t0 
left join rank_name as t1 
on t0.name = t1.name 
and t0.namespace = t1.namespace