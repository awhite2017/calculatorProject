from Myro import *
def add(num1, num2): #addition
    result = num1;
    for x in range(0,num2):
        print(x)
        result = result +1
    return result
    
answer = add(12,12) #answer = 24
print(answer)

def sub(num1, num2): #subtraction
    result = num1;
    for x in range(0,num2):
        print(x)
        result = result -1
    return result
  
answer = sub(20,5) #answer = 15
print(answer)

def multiply(num1, num2): #multiplication
    result = 0;
    for x in range(num2):
        print(x)
        result = add(result, num1)
    return result
    
answer = multiply(5,5) #answer = 25
print(answer)
  
 
    