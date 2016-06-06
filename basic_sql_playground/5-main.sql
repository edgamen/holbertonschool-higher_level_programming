select distinct last_name
from Person
INNER JOIN TVShowPerson
      on Person.id = TVShowPerson.person_id
INNER JOIN TVShow
      on TVShowPerson.tvshow_id = TVShow.id
where TVShow.name = 'Game of Thrones'
order by last_name asc;
SELECT count(id) from Person where age > 30;
SELECT Person.id, Person.first_name, Person.last_name, Person.age, EyesColor.color, TVShow.name
from Person
INNER JOIN EyesColor
      on Person.id = EyesColor.person_id
NATURAL INNER JOIN TVShowPerson
INNER JOIN TVShow
      on TVShowPerson.tvshow_id = TVShow.id;
SELECT sum(age) from Person;
