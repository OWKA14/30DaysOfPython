# Day 5: 30 Days of python programming

data = [1, 2, 3, 4, 5]
print(data)
print(len(data))
print(data[0], data[2], data[4])
mixed_data_types = ['Owen', 21, 170, False, 'Kutilang Street']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
it_companies.append('Twitter')
it_companies.insert(4, 'Tesla')
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
it_companies.remove('IBM')
print(it_companies)
symbol = '#; '
it_companies_str = symbol.join(it_companies)
print(it_companies_str)
does_exist = 'Facebook' in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
it_companies_slice = it_companies[0:3]
print(it_companies_slice)
it_companies_slice = it_companies[-3:]
print(it_companies_slice)
it_companies_slice_middle = it_companies[3:5]
print(it_companies_slice_middle)
del it_companies[3:5]
print(it_companies)
del it_companies[-1]
print(it_companies)
del it_companies[:]
print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# Exercise: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print('Min age:', min_age)
print('Max age:', max_age)
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)
median_age = ages[len(ages) // 2]
print('Median age:', median_age)
average_age = sum(ages) / len(ages)
print('Average age:', average_age)
age_range = max_age - min_age
print('Age range:', age_range)
value_of_min = abs(min_age - average_age)
value_of_max = abs(max_age - average_age)
print('Value of min:', value_of_min)
print('Value of max:', value_of_max)
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'];
middle_index = len(countries) // 2
middle_country = countries[middle_index]
print('Middle country:', middle_country)
first_half_countries = countries[:middle_index]
print('First half of countries:', first_half_countries)
second_half_countries = countries[middle_index:]
print('Second half of countries:', second_half_countries)
unpacked_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *rest = unpacked_countries
print('First country:', first)
print('Second country:', second)
print('Third country:', third)
scandinavian_countries = unpacked_countries[3:]
print('Scandinavian countries:', scandinavian_countries)