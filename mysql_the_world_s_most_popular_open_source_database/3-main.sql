\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
select TVShow.name from TVShow join Season on (TVShow.id = Season.tvshow_id) where number = 4 order by name;
\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
select TVShow.name from TVShow join TVShowGenre on (TVShow.id = TVShowGenre.tvshow_id) join Genre on (TVShowGenre.genre_id = Genre.id) where Genre.name = 'Comedy' order by TVShow.name;
\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
select Actor.name from Actor join TVShowActor on (Actor.id = TVShowActor.actor_id) join TVShow on (TVShowActor.tvshow_id = TVShow.id) where TVShow.name = 'The Big Bang Theory' order by Actor.name;
\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
select Actor.name, count(TVShowActor.actor_id) from Actor join TVShowActor on (Actor.id = TVShowActor.actor_id) group by TVShowActor.actor_id order by count(TVShowActor.actor_id) desc limit 10;
