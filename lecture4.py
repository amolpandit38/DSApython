print("hello World")
print("Amol", "Pandit", sep="*", end="\n")

# varible
age = 23
weight = 71.4
isAdult = True
name = "Amol"

# taking input
your_name = input("What is your name? ")
print(your_name)

birth_year = input("What is your birth year? ")
print(type(birth_year))
birth_year = int(birth_year)
print(2023-birth_year)


#String
name = "Amol pandit"
print(name.capitalize())
print(name.upper())


# list
list = [1, 2, 3, 4, 5]
list.insert(0, 7)
list.append(9)
list.extend([10, 20, 30])
list.clear()
print(list)
print(sum(list))
