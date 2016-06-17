\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
select TVShow.name, count(Season.id) as nb_seasons from Season join TVShow on (Season.tvshow_id = TVShow.id) group by tvshow_id order by name;
\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
select TVShow.name as 'TVShow name', Network.name as 'Network name' from TVShow join Network on (TVShow.network_id = Network.id) order by TVShow.name;
\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
select TVShow.name from TVShow join Network on (TVShow.network_id = Network.id) where Network.name = 'FOX (US)';
