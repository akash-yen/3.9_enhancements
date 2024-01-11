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

def add_str(x:str,y:str) -> str:
    return x+y

print(add_str.__annotations__)

#{'x': <class 'str'>, 'y': <class 'str'>, 'return': <class 'str'>}


a: int = 10


# for list , Tuple , Set we need use typing module

from typing import List

names : List[str] = ['akash','prudhvi']

def get_names() -> List[str]:
    names: List[str] = []
    names.append('akash')
    names.append('Prudhvi')
    names.append(10)

    return names

def sum(a: int,b:int) -> None:
    print(a+b)
def f1(f: callable[[int,int],None],x: int,y:int) -> None:
    f(x,y)

f1(sum,10,20)


# multiple data types

from typing import Union

def f1(x: Union[int,float]) -> None:
    print(x)

# optional is an alternative for either int or None return type




