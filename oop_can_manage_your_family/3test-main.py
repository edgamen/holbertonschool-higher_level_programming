from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

my_family_contents = load_from_file("my_family.json")
#my_family_contents = json.dumps([{"first_name": 'Rona', "last_name": 'Chong', "genre": 'Female', "date_of_birth": [12, 24, 1993], "eyes_color": 'Brown', "id": 20}])
print my_family_contents
save_to_file(my_family_contents, "my_family.json")
