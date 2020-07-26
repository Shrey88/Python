from named_tuple_intro import basic_plants_list, named_plants_list

print(named_plants_list[0])

""" *
    *   the basic plant list contains the tuples and 
    *   here we are tyring to access them based on the index
    * """
for plant in basic_plants_list:
    print(plant[0])

""" *
    *   named plant list contains the named tuples of types
    * """
for plant in named_plants_list:
    print(plant.name)

""" *
    *   named tuples are immutable but you can use the underscore replace function
    *   as a short and convenient way to create a new tuple with some values changed.
    * """
# you can create a new tuple like this
example = named_plants_list[0]
# print(example)
example = example._replace(lifecycle='Annual')
# print(example)

# you can also replace a value for the name tuple directly into the existing list
print(named_plants_list[0])
named_plants_list[0] = named_plants_list[0]._replace(lifecycle='Annual')
print(named_plants_list[0])