#write a program that will take 2 numbers and it will print the biggest number of them
"""x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("The biggest number is " + str(x))
else:
    print("The biggest number is " + str(y))"""

# askisi 5 : write a program that will 3 different numbers and it will return the biggest number among them
'''x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number :"))

if x >= y and x >= z:
    print("The biggest number is " + str(x))
elif y >= x and y >= z:
    print("The biggest number is " + str(y))
else:
    print("The biggest number is " + str(z))'''

#second way to solve it
"""x = int(input("Enter first number: "))

maximum = x

y = int(input("Enter second number: "))

if y > maximum :
    maximum = y

z = int(input("Enter third number :"))

if z > maximum:
    maximum = z

print(maximum)"""

#askisi 7 duo tupoi rixnoun apo 2 zaria o kathenas- ftiakse ena programma pou tha dexetai to athroisma ton zarion
"""p11 = 1
p12 = 1
p21 = 3
p22 = 2

if p11 + p12 < p22 + p21:
    print("Nikitis einai o Deuteros paixtis")
elif p11 + p12 > p21 + p22:
    print("Nikitis einai o Prwtos paixtis")
else:
    print("Isopalia rikse ksana")"""

#abbreviation of if statement
"""
x = 100
result = "mexnumber" if x > 10 else "minnumber"
print(result)"""

#askisi 8
hours = int(input("Dwse tin ora: "))
minutes = int(input("Dwse ta lepta: "))
seconds = int(input("Dwse ta deuterolepta: "))

if hours <10:
    message1 = "0" + str(hours)
else:
    message1 = str(hours)

if minutes < 10:
    message2 = "0" + str(minutes)
else:
    message2 = str(minutes)
if seconds <10:
    message3 = "0" + str(seconds)
else:
    message3 = str(seconds)

message = message1 + ":" + message2 + ":" + message3
print(message)