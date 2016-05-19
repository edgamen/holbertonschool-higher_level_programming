from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

r = Teenager(3, "Tony", [7, 4, 2015], "Male", "Green")
print r.json()
json = {'first_name': 'Rona', 'last_name': 'Chong', 'genre': 'Female', 'date_of_birth': [12, 24, 1993], 'eyes_color': 'Brown', 'id': 20}
r.load_from_json(json)
print r.json()

my_family = load_from_file("my_family.json")
print my_family
print "I have %d members in my family" % len(my_family)

# new baby!
b = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
b.last_name = "Foto"
print b.json()
my_family.append(b.json())
#print my_family

save_to_file(my_family, "my_family.json")
my_family = load_from_file("my_family.json")
print my_family
