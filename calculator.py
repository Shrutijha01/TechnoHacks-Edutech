def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return"Error! division by zero."
    else:
        return x/y
        
print("select operations:")
print("1. Addition")
print("2. subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    select = input("Enter choice(1/2/3/4):")

    if select in ('1', '2', '3', '4'):
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))

        if select == '1':
            print("Result:", add(num1, num2))
        elif select == '2':
            print("Result:", subtract(num1, num2))
        elif select == '3':
            print("Result:", multiply(num1, num2))
        elif select == '4':
             print("Result:", divide(num1, num2))
    else:
        print("Invalid Input")

    next_calculation = input("Do you want to perform another calculation? (yes/no):")
    if next_calculation.lower() != 'yes':
        break




