number_1 = int(input("Give first number: "))
number_2 = int(input("Give second number: "))
opr = input("Give operator (+, -, *, /): ")

if opr == "/" and number_2 == 0:
    print("Error! Cannot divide by zero! ❌")
elif opr == "+":
    result = number_1 + number_2
    print(f"Your answer is {result}")
elif opr == "-":
    result = number_1 - number_2
    print(f"Your answer is {result}")
elif opr == "*":
    result = number_1 * number_2
    print(f"Your answer is {result}")
elif opr == "/":
    result = number_1 / number_2
    print(f"Your answer is {result}")
else:
    print("Invalid operator! Please use +, -, *, /")