select
    row_number() over (order by channel_name) as channel_key,
    channel_name,
    min(message_date) as first_post_date,
    max(message_date) as last_post_date,
    count(*) as total_posts,
    avg(views) as avg_views
from {{ ref('stg_telegram_messages') }}
group by channel_name