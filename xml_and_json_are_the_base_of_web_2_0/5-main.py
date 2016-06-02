import json
from xml.dom.minidom import Document
from car import Car

''' FUNCTION DEFINITIONS '''
# return the number of different brands of a list of cars
def count_brands(car_list):
    if not isinstance(car_list, list):
        raise Exception("Expected a list of cars")

    list_brands = []
    for car in car_list:
        if not isinstance(car, Car):
            raise Exception("Expected a list of cars")
        car_brand = car.get_brand()
        if car_brand not in list_brands:
            list_brands.append(car_brand)

    return len(list_brands)

# return the cumulative number of doors for all cars
def count_doors(car_list):
    if not isinstance(car_list, list):
        raise Exception("Expected a list of cars")

    doors = 0
    for car in car_list:
        if not isinstance(car, Car):
            raise Exception("Expected a list of cars")
        doors += car.get_nb_doors()

    return doors

''' START PYTHON SCRIPT'''
file = open("5-main.json", 'r')
json_str = file.read()
file.close()

parsed_list = json.loads(json_str)

car_list = []
for car_hash in parsed_list:
    new_car = Car(car_hash)
    car_list.append(new_car)

print count_brands(car_list)
print count_doors(car_list)
print car_list[3]

doc = Document()
cars = doc.createElement('cars')
doc.appendChild(cars)
for car in car_list:
    car_xml = car.to_xml_node(doc)
    cars.appendChild(car_xml)
print doc.toxml(encoding='utf-8')
