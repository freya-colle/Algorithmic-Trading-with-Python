"""
Types of Object
(1) Number
(2) String
(3) Logical Operations and Boolean
(4) Variable assignment
(5) Tuples and List
(6) Dictionary
(7) Set
"""
#NUMBERS and STRING and VARIABLE ASSIGNMENT
a = float(input('a = ',))
b = float(input('b = ',))
c = a + b
c1 = a - b
c2 = a*b
d = a**2
d1 = a**3
e = a/b
e1 = a//b
string1 = f'ADDITION: {a} + {b} = {c}'
print(f'ADDITION: {a} + {b} = {c}') #F_STRING
print('ADDITION: {} + {} = {}'.format(a, b, c))
print(f'SUBTRACTION: {a} - {b} = {c1}')
print(f'MULTIPLICATION: {a}*{b} = {c2}')
print(f'DIVISION: {a}/{b} = {e}')
print(f'WHOLE DIVISION: {a}/{b} = {e1}')
print(f'POWER: {a}**2 = {d}, {a}**3={d1}')
print('MODULO: 16 = 5*3 + 1, 16%3 =', 16%3)
print(string1[0:1]) #SLICING
print(f'Check if {a} > {b} :', a > b)
print(f'Check if {a} == {b} :', a == b)
print(f'Check if {a} < {b} :', a < b)
print(f'Check if {a} != {b}', a != b)
print(f'{a} > {b} and {b} < {c}', a > b and b < c)
print(f'{a} > {b} or {b} < {c}', a > b or b < c)
print(f'not {a} > {b} and {b} < {c}', not a > b and b < c) #NOT
print(f'not {a} > {b} or {b} < {c}', not a > b or b < c)
price = float(input('price:',))
date = input('date: ',)
print(f'Tesla price is {price} at {date}')
time = input('time: ',)
market_open = ("09:00" <= time <= "11:30") or ("13:00" <= time <= "15:00")
print(market_open)




