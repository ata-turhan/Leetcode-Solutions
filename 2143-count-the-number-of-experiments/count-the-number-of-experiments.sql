with platforms as (
    select "Android" as platform
    union
    select "IOS" as platform
    union
    select "Web" as platform
),
experiment_names as (
    select "Reading" as experiment_name 
    union
    select "Sports" as experiment_name 
    union
    select "Programming" as experiment_name 
),
platforms_and_experiment_names as (
    select * from platforms, experiment_names
),
grpd_experiments as (
    select platform , experiment_name, count(experiment_id) as num_experiments from Experiments group by platform, experiment_name
)

select platforms_and_experiment_names.platform, platforms_and_experiment_names.experiment_name, ifnull(grpd_experiments.num_experiments , 0) as num_experiments from platforms_and_experiment_names left join grpd_experiments using(platform, experiment_name)
