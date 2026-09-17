# input
username = input("Enter your name: ")
height_cm = float(input("Enter your height in cm: "))

# calculations
INCH = 2.54
height_m = height_cm / 100
height_in = round((height_cm / INCH), 2)

# output 
print("Hello " + username)
print("Your height is " + str(height_m) + "m.")
print("That is " + str(height_in) + " inches.")
print("Taller than 180cm: " + str(height_cm > 180))