\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
select TVShow.name, count(Season.id) as nb_seasons from Season join TVShow on (Season.tvshow_id = TVShow.id) group by tvshow_id order by name;
