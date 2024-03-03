#100 days of code: The copmplete Python Pro Bootcamp

#Tip calculator - day 2 project

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))

tip = int(input(f"What percantage tip would you like to give? ")) / 100

people = int(input(f"How many people to split the bill? "))

result = ((total_bill + total_bill*tip)/people)

print(f"Each person should pay: $" + "{:.2f}".format(result))

