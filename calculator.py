def add(a,b):
    return a+b
def sub(a,b):
   return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Error: Not Division By Zero"
def mod(a,b):
   return a%b
def exponentiation(a,b):
   return a**b
def floordivision(a,b):
    return a//b
    
a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
operation=input("Choose operation(+,-,*,/,%,**,//)= ")

if operation=="+":
    result=add(a,b)
    
elif operation=="-":
    result=sub(a,b)
    
elif operation=="*":
    result=mul(a,b)
    
elif operation=="/":
    result=div(a,b)
    
elif operation=="%":
    result=sub(a,b)
    
elif operation=="**":
    result=sub(a,b)
    
elif operation=="//":
    result=sub(a,b)
    
else:
    print("error:Invalid operation")
    exit()
print(f"Result: {result}")

