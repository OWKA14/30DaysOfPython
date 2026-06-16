# Day 2: 30 Days of python programming

first_name = 'Owen'
last_name = 'Kartika'
full_name = 'Owen Kurniawan Kartika'
country = 'Indonesia'
city = 'Singaraja'
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
first_name, last_name, country, age = 'Owen', 'Kartika', 'Indonesia', 21

print(type(first_name))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

# The radius of a circle is 30 meters. Calculate the area of the circle and circumference of the circle
radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print(area_of_circle)
print(circum_of_circle)

input_radius = input('Enter radius: ')
area_of_circle = 3.14 * int(input_radius) ** 2
circum_of_circle = 2 * 3.14 * int(input_radius)
print(area_of_circle)
print(circum_of_circle)

# built in input function
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you from? ')
age = input('How old are you? ')
print('Your first name is ' + first_name)
print('Your last name is ' + last_name)
print('You are from ' + country)
print('You are ' + age + ' years old')

help('keywords')