select
    m.message_id,
    c.channel_key,
    cast(to_char(m.message_date, 'YYYYMMDD') as integer) as date_key,
    m.message_text,
    m.message_length,
    m.views,
    m.forwards,
    m.has_image,
    m.image_path
from {{ ref('stg_telegram_messages') }} m
left join {{ ref('dim_channels') }} c
    on m.channel_name = c.channel_name