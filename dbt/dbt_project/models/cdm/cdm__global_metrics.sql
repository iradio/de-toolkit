{{
    config(
        materialized='incremental'
    )
}}

with chargeback as (
    select operation_id 
    from {{source('de', 'transactions')}} t
    where status = 'chargeback'
),
r as (
    select 
    to_char(t.transaction_dt,'yyyy-mm-dd') as transaction_day
    , t.operation_id
    ,t.currency_code as  currency_from
    , t.amount as amount 
    , COALESCE(c.currency_with_div, 1) as usd_currency_div
    , account_number_from as account_make_transaction
    from {{source('de', 'transactions')}} t
    left join chargeback cb using (operation_id)
    left join {{source('de', 'currencies')}} c 
        on to_char(c.date_update,'yyyy-mm-dd') = to_char(t.transaction_dt,'yyyy-mm-dd')
                        and c.currency_code_with = 420 -- выбираем курс к доллару
                        and t.currency_code  = c.currency_code
    where cb.operation_id is null
{% if is_incremental() %}
        and date(t.transaction_dt) > coalesce(
            (select date_update as date from {{ this }} cgm order by date_update desc limit 1)
            ,date('2000-01-01')
            )
{% endif %}
        and account_number_from > 0 -- убираем тестовые аккаунты
        and account_number_to > 0 -- убираем тестовые аккаунты
        and t.status = 'done' -- оставляем только завершенные транзакции
        and t.transaction_type in ('c2a_incoming',
                                    'c2b_partner_incoming',
                                    'sbp_incoming',
                                    'sbp_outgoing',
                                    'transfer_incoming',
                                    'transfer_outgoing')
    order by t.operation_id
) 
select 
    to_date(r.transaction_day,'yyyy-mm-dd') as date_update
    , r.currency_from::int as currency_from
    , sum(r.amount * r.usd_currency_div)::numeric(18,2) as amount_total 
    , count(distinct operation_id)::int as cnt_transactions
    , count(distinct account_make_transaction)::int as cnt_accounts_make_transactions 
    , (count(distinct operation_id)::int / count(distinct account_make_transaction)::int)::numeric(16,2) as avg_transactions_per_account
from r
group by r.transaction_day, r.currency_from
order by r.transaction_day, r.currency_from