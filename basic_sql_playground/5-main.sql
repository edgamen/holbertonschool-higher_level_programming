select distinct last_name
from Person
INNER JOIN TVShowPerson
      on Person.id = TVShowPerson.person_id
INNER JOIN TVShow
      on TVShowPerson.tvshow_id = TVShow.id
where TVShow.name = 'Game of Thrones'
order by last_name asc;
