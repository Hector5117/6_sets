# sets
#definicion  son un conjunto de valores no ordenados que no se duplican




my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario

my_other_set = {"Hector", "Sanchez", 32}
print(type(my_other_set))

print(len(my_other_set))

#insercion

my_other_set.add("HectorDev")

print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("HectorDev") #Un set no admite repetidos

print(my_other_set)

#busqueda

print("Hector" in my_other_set)
print("Heector" in my_other_set)

#Eliminacion

my_other_set.remove("Sanchez")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) #name 'my_other_set' is not defined

#Transformacion  # el set sale en {} el list en []

my_set = {"Hector", "Sanchez", 32}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))