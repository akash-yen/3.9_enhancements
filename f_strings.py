#f_strings or formatted strings or literal string interpolation

# 3- types of techiniques

# %- formatiing
# str.format()
# f-strings

name = 'Akash'
s = 'hello %s, Good Morning' %name
s = 'Hello {}, Good Morning'.format(name)

# Dictinory as string format
student = { 'name' : 'Akash',
            'father_name' : 'Ramana',
            'mother_name' : 'Srinija',
            'School' : 'IU'
}

s = 'Hello {name}, you are the most luckiest one as you have father {father_name}, {mother_name} and school {School}'.format(**student)
print(s)

# f-string

s = f'Hello {name}, good evening'# u can use F as well or '' or ''' or """ is also valid

print(s)

# Processing dict data in f string

student = { 'name' : 'Akash',
            'father_name' : 'Ramana',
            'mother_name' : 'Srinija',
            'School' : 'IU'
}

s = f"Hello {student['name']}, you are the most luckiest as your father {student['father_name']}, mother{student['mother_name']}, scholl{student['School']}" # double quates is best when using anothe '
print(s)

name = 'akash'
s = f'my name is {name.upper()}'
print(s)

a=10
b=20
c=30
print(f'the resutls : {10*20/30}')
print(f'the resutls : {10*20/30:.2f}')
print(f'the resutls : {a*b/c}')

print(f'check {{ this') # only one { is printed
#print(f'check {{{ this') # error as pvm is looking for }

name = 'akash'
print(f'Name:{name}') # akash
print(f'Name:{{name}}') # {name}
print(f'Name:{{{name}}}') # {akash}
print(f'Name:{{{{name}}}}') # {{name}}

# 3.8 version enhancements related to f-strings

# we can use = symbol inside f-string for self documenting expressions and it is very useful for debugging purpose

x = 10
y=30
print(f'{x=}')
print(f'{y=}')


name = 'akash'
sal = 10000
college = 'iu'

print(f'{name=},{sal=},{college=}')
