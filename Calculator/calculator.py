type = input(" Enter the type of operation: ")
 #+, -, * or /
num1 = float(input(".Enter the first number: "))
num2 = float(input(".Enter the second number: "))
if type == "+":
    print("")
    print("result:", num1 + num2)
elif type == "-":
    print("")
    print("result:", num1 - num2)
elif type == "*":
    print("")
    print("result:", num1 * num2)
elif type == "/":
    print("")
    print("result:", num1 / num2)
else:
    print("Invalid Operation!!!!!!!")
input("")
