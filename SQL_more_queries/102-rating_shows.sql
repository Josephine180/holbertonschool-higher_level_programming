-- lists all shows 
-- by their rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating sum
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating sum DESC;