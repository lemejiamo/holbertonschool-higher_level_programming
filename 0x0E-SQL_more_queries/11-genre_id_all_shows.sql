-- all shows by genre id
SELECT tv_shows.title, tsg.genre_id
	FROM tv_shows
	LEFT JOIN tv_show_genres AS tsg
	ON tsg.show_id=tv_shows.id
	ORDER BY tv_shows.title, tsg.genre_id ASC;

