\! echo "\nNumber of seasons by tvshow_id?"
select tvshow_id, count(id) from Season group by tvshow_id;
\!echo "\nNumber of occurrences of the same episode number ordered by episode number?"
select number, count(id) from Episode group by number order by number;
