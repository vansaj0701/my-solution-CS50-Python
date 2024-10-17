#INPUT MASS FROM USER AND SAVING IT TO "mass" VARIABLE
#REMOVE WHITESPACES
mass = int(input("Enter mass(in kilograms): "))

#VALUE OF SPEED OF LIGHT
c = 300000000

#E = m*c*c
#STORING RESULT IN "energy" VARIABLE
energy = mass * c * c

#PRINT RESULT
print(f"Energy is {energy}")
