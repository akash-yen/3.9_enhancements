#static type checking is possible bcz of type hints
#we can declare the type for variables
#we can declare the type for fun arguments
#we can declare the type for return values

# Function related types hints or function annotations:

def add(x,y):
    print(x+y)

def add(x :int,y: int) -> None:
    print(x+y)

# python won't check u need to install  pip install mypy
# py -m mypy test.py
#or
#mypy test.py
