with source as (

    select *
    from raw.telegram_messages

),

cleaned as (

    select
        message_id,
        channel_name,
        cast(message_date as timestamp) as message_date,
        message_text,
        length(message_text) as message_length,
        has_media as has_image,
        image_path,
        coalesce(views, 0) as views,
        coalesce(forwards, 0) as forwards
    from source
    where message_id is not null

)

select * from cleaned