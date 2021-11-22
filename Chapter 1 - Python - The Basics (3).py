"""
Chapter 1:
- Python structure: If, Elif, Else
- Loop: For, While
"""

###IF
x = float(input('x = ', ))
if x < 5:
    print("Yes, x < 5")
else:
    print("No, x >= 5")

###IF, ELIF
if 10 < x < 99:
    print('10 < x < 99')
elif x < 10:
    print('x < 10')
else:
    print('x = 10 or x >= 99')
###FOR LOOP
sequence2 = [9, 3, 2, 3]
print(sequence2)
for sequence in sequence2: #Loop for sequence, list
    print(sequence)

for i in range(9): #Loop for range
    print('i in range(9): ', i)

###WHILE LOOP
d = int(input('d = ', ))
while d <= 15:
    print(d)
    d = d +1




