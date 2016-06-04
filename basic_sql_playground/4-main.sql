insert into EyesColor values ((select id from Person where first_name = 'Jon' and last_name = 'Snow'), 'Brown');
insert into EyesColor values ((select id from Person where first_name = 'Arya' and last_name = 'Stark'), 'Green');
create table TVShow (
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       name char(128) NOT NULL);
create table TVShowPerson (
       tvshow_id INTEGER NOT NULL,
       person_id INTEGER NOT NULL,
       FOREIGN KEY(tvshow_id) REFERENCES TVShow(id), 
       FOREIGN KEY (person_id) REFERENCES Person(id)
);
insert into TVShow (name) values
       ('Homeland'),
       ('The big bang theory'),
       ('Game of Thrones'),
       ('Breaking bad');
insert into TVShowPerson (tvshow_id, person_id) values
       ( (select id from TVShow where name = 'Breaking bad'), (select id from Person where first_name = 'Walter Junior' and last_name = 'White') ),
       ( (select id from TVShow where name = 'Game of Thrones'), (select id from Person where first_name = 'Jaime' and last_name = 'Lannister') ),
       ( (select id from TVShow where name = 'The big bang theory'), (select id from Person where first_name = 'Sheldon' and last_name = 'Cooper') ),
       ( (select id from TVShow where name = 'Game of Thrones'), (select id from Person where first_name = 'Tyrion' and last_name = 'Lannister') ),
       ( (select id from TVShow where name = 'Game of Thrones'), (select id from Person where first_name = 'Jon' and last_name = 'Snow') ),
       ( (select id from TVShow where name = 'Game of Thrones'), (select id from Person where first_name = 'Arya' and last_name = 'Stark') );
select * from Person;
select * from EyesColor;
select * from TVShow;
select * from TVShowPerson;
