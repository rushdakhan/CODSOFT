def add(a,b):
   return a+b

def sub(a,b):
   return a-b

def mult(a,b):
   return a*b

def div(a,b):
   try:
     return a / b
   except ZeroDivisionError:
      print("Sorry! Cannot divide by zero")

print("Calculator!!")
num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))

print("Please Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

ch = input("Enter choice (1/2/3/4): ")
if ch=='1':
    print("Result: " , num1, "+", num2, "=", add(num1, num2))
elif ch=='2':
   print("Result: " , num1, "-", num2, "=", sub(num1, num2)) 
elif ch=='3':
   print("Result: " , num1, "x", num2, "=", mult(num1, num2))
elif ch=='4':
   print("Result: " , num1, "/", num2, "=", div(num1, num2))
else:
   print("Invalid Input")