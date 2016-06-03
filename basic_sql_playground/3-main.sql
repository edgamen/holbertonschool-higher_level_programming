update Person set age = 27 where first_name = 'Jon' and last_name = 'Snow';
update Person set age = 18 where first_name = 'Walter Junior' and last_name = 'White';
delete from Person where first_name = 'Walter' and last_name = 'White';
-- need to find out how to delete entry in the other table
select * from Person order by first_name asc;
