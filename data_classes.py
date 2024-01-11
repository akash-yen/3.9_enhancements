from dataclasses import dataclass

@dataclass # or @dataclass() # or @dataclass(init=True,repr=True,eq=True, order = False, frozen = False)
class Employee:
    eno : int
    ename : str
    esal : int
    eaddr : str

#order usually it is false < , > , >= , <= (i.e __lt__, __gt__, __le__, __ge__)
# frozen is also False by default if frozen is true u cant update values
e1 = Employee(100,'akash',10000,'IU')
e2 = Employee(123,'asdf',10000,'IU')
e3 = Employee(100,'akash',10000,'IU')

print(e1.ename)
print(e1) # even __repr__ is taken care
print(e1==e2) # False
print(e1==e3) # True # __eq is also taken care
print(e3)