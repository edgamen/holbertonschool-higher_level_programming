\! echo "Number of seasons by tvshow_id?"
select tvshow_id, count(id) from Season group by tvshow_id;
