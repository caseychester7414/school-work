# this is extra 1 
print("This program will help you to divide")
num1 = input("Give me the numerator: ")
num2 = input("Give me the denominator: ")

if int(num1) % 4 == 0:
    print("DYK your " +num1 + " numerator is divisible by 4")
elif int(num1) % 2 == 0:
    print("DYK your " +num1 + " numerator is divisible by 2 meaning an even digit")
else:
    print("DYK your " +num1 + " numerator is NOT divisible by 2 meaning an odd digit")

if int(num1) % int(num2) == 0:
    print("Numerator " + num1 + " is completely divisible by denominator " + num2)
else:
    print("Numerator " + num1 + " is NOT divisible by denominator " + num2)