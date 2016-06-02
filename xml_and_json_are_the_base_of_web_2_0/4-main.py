from car import Car

c = Car(name="Rogue", brand="Nissan", nb_doors=5)
print c
c_json_string = c.to_json_string()
print type(c_json_string)
print c_json_string
