-- Get the genre_id for the show 'Dexter'
SET @dexter_genre_id = (SELECT genre_id FROM tv_shows WHERE title = 'Dexter');

-- List all genres not linked to the show 'Dexter'
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_shows ON tv_genres.id = tv_shows.genre_id AND tv_shows.genre_id = @dexter_genre_id
WHERE tv_shows.genre_id IS NULL
ORDER BY tv_genres.name ASC;
