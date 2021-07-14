-- Lists all genres.
SELECT tg.name AS genre,
       COUNT(tsg.genre_id) AS number_of_shows FROM tv_genres AS tg
       JOIN tv_show_genres AS tsg
       ON tg.id=tsg.genre_id
       GROUP BY tsg.genre_id
       ORDER BY number_of_shows DESC;
