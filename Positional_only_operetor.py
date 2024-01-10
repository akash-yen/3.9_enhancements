def f1(*,a,b): # all parametres after * it will become kw only parameters
    print(a,b)
f1(a= 0,b = 20)

# posistional only arguments

# /--> forward slash all parametrs before / are postionla only

def f1(a,b,/):
    print(a,b)

f1(10,20) # this will help if in case an api orginal parameter name is changed
# if you want to secure the parameter names
# in oops while overriding parent and child class
#performance improvement
# most inbuilt funs are implemeted in c language which uses positional arguments


