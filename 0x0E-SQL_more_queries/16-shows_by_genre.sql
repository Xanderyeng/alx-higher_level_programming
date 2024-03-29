-- List all shows and their linked genres (or NULL) --
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, name ASC;
