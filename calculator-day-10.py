#100 days of code: The copmplete Python Pro Bootcamp

#Simple calculator - day 10 project

def input_data(num1):
    if num1==None:
        num1 = float(input("What's the first number?: "))
    operation = input("Pick an operation (+, -, *, /): ")
    num2 = float(input("What's the next number?: "))
    return num1, operation, num2

def add(num1, num2):
    end_num = num1 + num2
    return end_num

def subtract(num1, num2):
    end_num = num1 - num2
    return end_num

def multiply(num1, num2):
    end_num = num1 * num2
    return end_num

def divide(num1, num2):
    end_num = num1 / num2
    return end_num

def calculate_operation(num1, operation, num2):
    if operation == "+":
        end_num = add(num1, num2)
    elif operation == "-":
        end_num = subtract(num1, num2)
    elif operation == "*":
        end_num = multiply(num1, num2)
    elif operation == "/":
        end_num = divide(num1, num2)
    else:
        print("Check provided data (operation type)")
    return end_num

def continue_or_stop(end_num):
    decision = input(f"Type 'y' to continue calculating with {end_num}, or type 'n' to start a new calculation: ")
    if decision == "n":
        next_num = None
        continue_calculation = True
        return continue_calculation, next_num
    elif decision == "y":
        next_num = end_num
        continue_calculation = True
        return continue_calculation, next_num
    else:
        next_num = None
        continue_calculation = False
        print("Closing calculator")
        return continue_calculation, next_num
        
        
def main():
    continue_calculation = True
    num1=None
    while continue_calculation:
        num1, operation, num2 = input_data(num1)
        end_num = calculate_operation(num1, operation, num2)
        print(end_num)
        continue_calculation, num1 = continue_or_stop(end_num)

main()