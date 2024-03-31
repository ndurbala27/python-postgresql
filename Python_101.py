#x=5
#print(x)

#age = 5
#print(age)

#print(age + " years")
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#convert number to string
#age_string = str(age)
#print(age_string)
#print(age_string + " years")
#print(str(age) + " years")

#convert age in years to days
#print(age*365)

#convert age in days to hours
#print(age*365*24)

#convert age in hours to minutes
#print(age*365*24*60)

#convert age in minutes to seconds
#print(age*365*24*60*60)

age = input('Enter your age: ')
#print('You have lived for ' + str(int(age)*365*24*60*60) + ' seconds.')

#using format method
print('You have lived for {} seconds. This corresponds to {} years.'.format(int(age)*365*24*60*60, age))