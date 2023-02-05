#hours = int(input("Enter hours:"))
#rate_per_hour = int(input("Enter rate per hour:"))
#weekly_earning = hours*rate_per_hour
#print(weekly_earning)

#years = int(input("Enter the number of years you have lived:"))
#seconds = years * (365*24*60*60)
#print("the number of years lived in seconds are: %d " %seconds)

# for i in range (1,3):
#     print(i, int(i/i), i, i*i, i*i*i)

# multi_string = '''the day is beatiful
# i am going to get a lot done
# progress on day tasks'''

# print(multi_string)




# from itertools import count


# first= 'akshata balhara loves aryan'
# # space = ' '
# last ='balhara'
# bae = 'aryan'
# # total = first + space + last
# # print(total)
# # print(len(first) == len(last))

#total = 'I am %s %s and I love %s %s to the moon and back' %(first, last, bae, last)
#total = f'I am {first} {last} and I love {bae} {last} to the moon and back'
#total = 'I am {} {} and I love {} {} to the moonand back'.format( first, last,bae, last)
#print(total)
# first_letter = first[0]
# last_letter = len(first) -1
# last_let = first[last_letter]
# print(first_letter, last_let)
# print(first[1:4])
# print(last[2:])

#print(first.rfind('a'))
#print(first.strip('ha'))

#print(first.split(','))

# string1 = 'coding'
# string2 = 'for'
# string3 ='all'
# total = string1 + ' ' + string2 + ' ' + string3
# company = total
# biz = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# stuff = 'You cannot end a sentence with because because because is a conjunction'
# space = '   Coding For All      '
# # print(company.find('c'))
# # slice = stuff[31:47]
# # print(company.startswith('coding'))

# print(space.strip())

# print(company)
# print(company.lower())
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())
# print(company.strip('slice'))
# print(company.find('coding'))
# print(company.replace('coding', 'python'))
# print(biz.split(','))




# text = company.split()
# a = " "
# for i in text:
#     a = a+str(i[0]).upper()
# print(a)

# a = 8
# b = 6
# print( f'{a} + {b} = {a + b}')

# love = ['aryan', 'bunny', 'bootycheeks', 'bbg']
# love[3] = 'babygoose'
# first, *rest, last= love
# lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
# #lovee = love.copy()
# lst.extend(love)
# print(lst)


# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages)
# min = ages[0]
# last = len(ages) -1
# max = ages[last]

# add = min + max
# print(min, max, add)
# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Cape Verde',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombi',
#   'Comoros',
#   'Congo (Brazzaville)',
#   'Congo',
#   'Costa Rica',
#   "Cote d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor Timur)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia, The',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Macedonia',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia and Montenegro',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Swaziland',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Taiwan',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe',
# ];

# middle_index = int(len(countries)/2)
# middle = countries[middle_index]
# print(middle)


# empty = tuple()
# print(empty)

# greek = ('achilles', 'patroclus', 'circe', 'odyseus')
# new_greek = ('ariandne', 'athena')
# myth = greek+ new_greek

# all = myth[0:4]
# print(all)
# # list = list(greek)
# # print(list)

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# value = 'Iceland' in nordic_countries
# print(value)

# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# #it_companies.add('Twitter')
# more_comp = {'AWS', 'Magic leap', 'Netflix'}
# it_companies.update(more_comp)

# it_companies.remove('IBM')
# print(it_companies)

# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# B.symmetric_difference(A)
# print(A)

# age = [22, 19, 24, 25, 26, 24, 25, 24]
# set = set(age)
# print(set)

# print(len(age) == len(set))

# string = 'I am a teacher and I love to inspire and teach people.'
# words = string.split()
# unique = set(words)
# print(len(unique))

# sentence = "I am a teacher and I love to inspire and teach people."
# words = sentence.split()
# unique_words = set(words)
# print(len(unique_words))

# person = {
#     'first_name':'Aryan',
#     'last_name':'Balhara',
#     'age':28,
#     'country':'Florida',
#     'is_marred':False,
#     'skills':['CAD', 'Design', 'Mechanical', 'Calibration', 'C'],
#     'address':{
#         'street':'Flagler Village',
#         'zipcode':'00334'
#         }
# }
# person['Girlfriend'] = True
# person.pop('is_marred')

# print(person.items())


# a=int(input("Enter a number:"))
# if (a > 0):
#     if (a % 2 == 0):
#         print('tis pos and even')
#     else:
#         print( 'a be pos but not even')
# elif a == 0:
#     print('a is zero')
# else:
#     print('a is neg')

# age = int(input('Enter your age:'))
# limit = 18
# if age >= 18:
#     print('You are old enough to learn to drive')
# else:
#     print('you need' + ' ' + str(limit - age) + ' ' 'more years to learn to drive' )

# my_age = int(input('Enter my age:'))
# your_age = int(input('Enter you age:'))
# age_diff = my_age - your_age

# if age_diff >0:
#     if age_diff ==1:
#         print('I am {age_diff} years older than you')
#     else:
#         print('I am {age_diff} years older than you')
# elif age_diff <0:
#     if age_diff == -1:
#         print(f'I am {abs(age_diff)} years older than you')
#     else:
#         print(f'I am {abs(age_diff)} years older than you')
# else:
#     print('we are the same age')

# a = int(input('Enter number a:'))
# b = int(input('Enter number b:'))

# if a>b:
#     print(f'{a} greater than {b}')
# elif b>a:
#     print(f'{b} greater than {a}')
# else:
#     print('they equal')


# marks = int(input('Enter the student score:'))

# if marks >= 80 and marks <=100:
#     print('grade is A')
# elif marks >= 70 and marks <=89:
#     print('grade is B')
# elif marks >= 60 and marks <=69:
#     print('grade is C')
# elif marks >= 50 and marks <=59:
#     print('grade is D')
# elif marks >= 40 and marks <=49:
#     print('grade is E')
# else:
#     print('grade is F')


# fruits = ['banana', 'orange', 'mango', 'lemon']

# frut = input('Enter a new fruit:')

# if frut in fruits:
#     print('Fruit already exists')
# else:
#     fruits.append(frut)
#     print(fruits)


# person={
#     'first_name': 'Aryan',
#     'last_name': 'Balhara',
#     'age': 29,
#     'country': 'America',
#     'is_marred': False,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# skills = person['skills']
# middle_skill = int(len(skills)/2)
# mid_skl = skills[middle_skill]

# if 'skills' in person:
#     print('The middle skill is:' mid_skl)
# else:
#     print('skills does not exist')


# count = 0

# while count<7:
#     if count == 4:
#         continue
#     print(count)
#     count = count + 1

# count = 0
# while count < 5:
   
    
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1

# string = 'Aryan'
# for alpha in string:
#     print(alpha)

# for i in range(len(string)):
#     print(string[i])


# for num in range(101):
#     if (num%2 != 0):
#         print(num)
        
    

# for numb in range(10,-1,-1):
#     print(numb)

# i =0
# while i < 11:
#     print(i)
#     i += 1

# i = '#'
# for j in range (0,7):
#     print( i * (j+1))

# i=0
# for i in range(0,11):
#     print(f'{i} x {i} = {i*i}')

# lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for item in lst:
#     print(item)


# sum=0
# for i in range(101):
#     sum += i
# print(sum)

# esum = 0
# osum = 0
# for i in range(101):
#     if i%2 == 0:
#         esum += i
#         print('sum of even numbers:', esum) 
#     else:
#         osum += i
#         print('sum of odd numbers:', osum)

# def bunny(bebe):
#     stuff = bebe + ',You are the cutest'
#     return stuff
# print(bunny('aryan'))

def even_num(n):
    even = []
    for i in range(n + 1):
        if i % 2 == 0:
            even.append(i)
        return even
print(even_num(10))

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))




    
    




