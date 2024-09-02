day_of_week = input("Enter the day of week: ").lower() #convert to lowercase

print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("I will learn DevOps")
else:
    print("I will practise DevOps")
num1 = int(input("Enter first number: ")) #str -> int is called Type Casting
num2 = int(input("Enter second number: "))

choice = input("Enter the opereations: (Options are +,-,*,/,%) : ")
if choice == "+":
    sum_of_num = num1 + num2
    print("Addition ",sum_of_num )
elif choice == "-":
    diff_of_num = num1 - num2
    print("Substraction ",diff_of_num)
elif choice == "*":
    product_of_num = num1 * num2
    print("Multiplication ",product_of_num)
elif choice == "/":
    division_of_num = num1 / num2
    print("Division ", division_of_num)
elif choice=="%":
    rem_of_num = num1 % num2
    print("Remainder ", rem_of_num)
else:
    print("Invalid Choice")