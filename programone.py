# pythonChapterThreeApprovedSolution.py
#
# Programmer Name: Matthew Gutierrez
# Date: 8/13/23

print("\n Welcome to Mac Mac's Largest of Three program!\n")

# Get user's name
user_name = input(" User input your name: ")

print ("\nThank you " + user_name + " !")

print ("\nNow I need a few numbers....\n")

# Get three integers from the user

num1 = int(input("Enter integer 1: "))

num2 = int(input("Enter integer 2: "))

num3 = int(input("Enter integer 3: "))

#Quotiant
q1 = int(num1)
q2 = int(num2)
print ("\nThe result of dividing integer 1 by integer 2 is")
print(q1/q2)
print(".....oops you didn't need to know that.\n")

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print("Hello, " + str(user_name) + "! The largest number is: " + str(largest) + " ....'-'.....")
print("\n......a.^0^.choo-put type" + str(type(num3)) + "\n...a.^0^.choo-put type " + str(type(num2)) + "\n...a.^0^.choo-put type " + str(type(num1)) + "\n..^_- ...a..nput type " + str(type(user_name)) + "\n\n.....I'm sorry I think I did a boolean....-_-.")
print("\nThank you user, but I must terminate.")