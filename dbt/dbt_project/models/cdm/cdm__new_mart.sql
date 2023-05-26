select * 
from {{ref('stg__new_table')}}
where datname = 'postgres'