# List datastructures

country = ["Kenya", "Bangladesh", "United States", "Tanzania", "Belarusian", "United Kingdom", "Uganda", "Kenya"]
numbers = [34, 6, 90, 31, 21, 9, 0, -2, 14, 1, 4]
country[0] = "Somalia"

numbers.sort()
print(country)
print(country[1])
country.sort()
print(country)
print(numbers)
# print(f"The numbers are {numbers.count()}")

# tuple datastructure
fruits = ("banana", "apple", "watermelon", "pinneapple", "avocado", "oranges")

print(fruits)
print(fruits[1])

# set datastructure

names = {"bob", "alice", "john", "mercy", "eric"}
names.discard("eric")

print(names)

# dictionaries datastructures

# key value pair

employers = {"name": "Eric", "age": 18, "salary": "200,000","country":["kenya","uganda","Tanzania","Belarusian"]}
employers.pop('name')
print(employers)
