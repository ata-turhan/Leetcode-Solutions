with answer_rates as (
    select question_id, row_number() over (order by sum(action = "answer")/sum(action = "show") desc, question_id asc) as rn from surveylog group by question_id
)
select question_id as survey_log from answer_rates where rn = 1 and question_id is not null
