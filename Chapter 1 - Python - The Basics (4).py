"""
Chapter 1: Function
- Basics
- Local Variable
- Global Variable
- Lambda function
"""
def my_second_function(x,x2, x3):
    return x + x2 + x3
print("Function's results: ",my_second_function(2, 3, 4))

def my_s_function(x, x9 = 9, x3 = 9): #default setting
    return x + x9 + x3
print(my_s_function(0))

#LOCAL AND GLOBAL VARIABLE
global2 = 22

def my_function2():
    local_variable2 = 99
    print(global2)

my_function2()
#GLOBALIZE THE FUNCTION
def my_function3():
    global2
    t = 99
    print(global2)

###LAMBDA FUNCTION - small anonymous function
lambda x8: x8**2 #create lambda
lis = [2, 3, 4, 5, 8, 9]
generator = map(lambda x8: x8**2, lis) #use MAP function to apply lambda to a list
print(list(generator))

