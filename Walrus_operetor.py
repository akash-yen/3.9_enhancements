# #Walrus Operator
# names = []
# name = input('asd')
# while name != 'done':
#     names.append(name)
#     name = input('input')
# print(names)

# names = []
# while (name := input('asd')) != 'done':
#     names.append(name)
# print(names)



# file = open('Test.txt','r')
# context = file.readline()
# while context != '':
#     print(context, end='')
#     context = file.readline()
# file.close()

file = open('Test.txt','r')
while (context := file.readline()) != '':
    print(context, end='')
file.close()
