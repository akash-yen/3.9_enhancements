# asserstion 2 types
#simple version --> assert condtional_expression
#argumented version  --> assert condtional_exp message

x = 10
#assert x== 11
assert x == 10 ,'the value should be 10'


#

def squareit(x):
    return x**x

assert squareit(2) == 4, 'the square of 2 is 4'
assert squareit(3) == 9, 'the square of 3 is 9'
