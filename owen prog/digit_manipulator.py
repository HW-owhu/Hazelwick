# input
NUMBER = int(input("Enter a 3-digit number: "))
x = NUMBER

# calculations
hundreds = x // 100
tens = (x // 10) - (hundreds * 10)
units = x % 10
sum_of_digits = hundreds + tens + units 
reversed_number = units*100 + tens*10 + hundreds

# output
print("Hundreds: " + str(hundreds))
print("Tens: "+ str(tens))
print("Units: "+ str(units))
print("Sum of digits: " + str(sum_of_digits))
print("Reversed: " + str(reversed_number))
print("Even number: " + str(x % 2 == 0))