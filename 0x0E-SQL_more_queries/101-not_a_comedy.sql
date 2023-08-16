-- List all shows without the genre 'Comedy'
SELECT tv_shows.title
FROM tv_shows
WHERE genre_id != @comedy_genre_id OR genre_id IS NULL
ORDER BY tv_shows.title ASC;
