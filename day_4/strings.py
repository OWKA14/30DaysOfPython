# Day 4: 30 Days of python programming

# String concatenation
first_word = 'Thirty'
second_word = 'Days'
third_word = 'Of'
fourth_word = 'Python'
concatenated_string = first_word + ' ' + second_word + ' ' + third_word + ' ' + fourth_word
print(concatenated_string)

# String formatting 
first_word = 'Coding'
second_word = 'For'
third_word = 'All'
formatted_string = first_word + ' ' + second_word + ' ' + third_word
print(formatted_string)
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
first_word = company[0:6]
print(first_word)
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print(company.replace('Coding For All', 'Python For Everyone'))
print(company.split())
it_company = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(it_company.split(', '))
print(company[0])
print(company[10])

# Acronym for 'Python For Everyone'
words = 'Python For Everyone'
acronym = words[0] + words[7] + words[11]
print(acronym)

# Acronym for 'Coding For All'
acronym = company[0] + company[7] + company[11]
print(acronym)

# using index to find the position of 'C' in 'Coding For All'
index_of_c = company.index('C')
print(index_of_c)

# using index to find the position of 'F' in 'Coding For All'
index_of_f = company.index('F')
print(index_of_f)

# using rindex to find the position of 'l' in 'Coding For All'
rindex_of_l = company.rindex('l')
print(rindex_of_l)

# using index to find the position of 'because' in 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
index_of_because = sentence.index('because')
print(index_of_because)

# using rindex to find the position of 'because' in 'You cannot end a sentence with because because because is a conjunction'
rindex_of_because = sentence.rindex('because')
print(rindex_of_because)

# slice out the prhase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[31:54]
print(sliced_phrase)

# find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurrence_of_because = sentence.find('because')
print(first_occurrence_of_because)

# slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[31:54]
print(sliced_phrase)

# does 'Coding For All' start with a substring 'Coding'?
print(company.startswith('Coding'))

# does 'Coding For All' end with a substring 'All'?
print(company.endswith('All'))

# remove the left and right trailing spaces in the string '   Coding For All      '
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip())

# which variable return True when we use the method isidentifier() on '30DaysOfPython' and 'thirty_days_of_python'
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# combining some of python libaries ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] using the join() method with a hash character '#' with space string in between each library name.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
combined_libraries = ' # '.join(python_libraries)
print(combined_libraries)

# use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

# use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {}'.format(radius, area))

# use the string formatting method to display the following:
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))