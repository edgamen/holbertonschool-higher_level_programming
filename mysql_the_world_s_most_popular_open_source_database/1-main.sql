\! echo "\nNumber of seasons by tvshow_id?"
select tvshow_id, count(id) from Season group by tvshow_id;
\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
select number, count(id) from Episode group by number order by number;
\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
select genre_id, count(genre_id) as occurrences_genre from TVShowGenre group by genre_id order by count(genre_id) desc limit 3;
