# Day 3: 30 Days of python programming

age = int(21)
height = float(1.75)
complex_num = complex(2, 3)

# Calculating area of triangle
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area_of_triangle = 0.5 * base * height
print('The area of the triangle is ' + str(area_of_triangle))

# Calculating perimeter of triangle
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter_of_triangle = side_a + side_b + side_c
print('The perimeter of the triangle is ' + str(perimeter_of_triangle))

# Calculating area of rectangle
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('The area of the rectangle is ' + str(area_of_rectangle))
print('The perimeter of the rectangle is ' + str(perimeter_of_rectangle))

# Calculating area of circle
radius = int(input('Enter radius: '))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print('The area of the circle is ' + str(area_of_circle))
print('The circumference of the circle is ' + str(circum_of_circle))

# Calculating slope, x-intercept and y-intercept of y = 2x - 2
x = int(input('Enter x: '))
y = 2 * x - 2
print('The slope is ' + str(2))
print('The x-intercept is ' + str(1))
print('The y-intercept is ' + str(-2))

# Calculating the slope of a line between points (2, 2) and (6, 10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('The slope of the line is ' + str(slope))
print('The Euclidean distance between the points is ' + str(euclidean_distance))

# Comparing the value of slope with the value of y-intercept
y_intercept = -2
if slope > y_intercept:
    print('The slope is greater than the y-intercept')
elif slope < y_intercept:
    print('The slope is less than the y-intercept')
else:
    print('The slope is equal to the y-intercept')

# Calculating the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x = int(input('Enter x: '))
y = x ** 2 + 6 * x + 9
print('The value of y is ' + str(y))

# Finding the length of the string 'python' and converting the value to float and string
string1 = 'python'
string2 = 'dragon'
length_string1 = len(string1)
length_string2 = len(string2)
print('The length of the string1 ' + string1 + ' is ' + str(length_string1))
print('The length of the string2 ' + string2 + ' is ' + str(length_string2))
print(not length_string1 == length_string2)

# Checking if 'on' is found in both 'python' and 'dragon'
print('on' in string1 and 'on' in string2)

# Checking if 'jargon' is in the sentence 'I hope this course is not full of jargon'
string3 = 'I hope this course is not full of jargon.'
print('jargon' in string3)

# false value of 'on' is found in both 'python' and 'dragon'
print(not 'on' in string1 and not 'on' in string2)

# Finding the length of the text 'python' and converting the value to float and string
length_string1 = len(string1)
print(length_string1)
print(float(length_string1))
print(str(length_string1))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('Enter a number: '))
if number % 2 == 0:
    print(str(number) + ' is an even number')
else:
    print(str(number) + ' is not an even number')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
if 7 // 3 == int(2.7):
    print('The floor division of 7 by 3 is equal to the int converted value of 2.7')
else:      
    print('The floor division of 7 by 3 is not equal to the int converted value of 2.7')

# Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print('The type of \'10\' is equal to the type of 10')
else:
    print('The type of \'10\' is not equal to the type of 10')

# Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print('int(\'9.8\') is equal to 10')
else:
    print('int(\'9.8\') is not equal to 10')

# Calculate pay of a person based on hours and rate per hour
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour:'))
pay = hours * rate_per_hour
print('The pay of the person is ' + str(pay))

# Calculate the number of seconds a person can live. Assume a person lives just hundred years
age = int(input('Enter number of years you have lived: '))
seconds_in_a_year = 365 * 24 * 60 * 60
seconds_lived = age * seconds_in_a_year
print('You have lived for ' + str(seconds_lived) + ' seconds')

# Print the following pattern
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')