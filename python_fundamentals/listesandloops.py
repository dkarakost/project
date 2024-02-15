'''i = 1
while i <= 10:
    print("Thuella")
    i += 1'''

'''Active = True
while Active:
    number = input("Input a number or quit ")
    if number == "quit":
        print("Bye Bye")
        Active= False
    else:
        number = float(number) ** 2
        print(number)'''

'''i = 0 # the program saves 10 numbers from the user and return the sum of them!
list = []
while i <= 9:
    i += 1
    number = int(input("Please enter the " + str(i) + "th number "))
    list.append(number)
print(sum(list))'''

'''
#prints the even numbers from 10 to 20
for number in range(10,21,2):
    print(number)
#prints the odd numbers from 19 to 11
for number in range(19,11,-2):
    print(number)
#prints the odd numbers from 1 to 30 that can also divided by 3 
for number in range(1,30,2):
    if number % 3 == 0:
        print(number)'''

'''cities = ["Thessaloniki", "Kilkis", "Athina", "Utrech", "Amsterdam"]

for index in range(0, len(cities), 2):
    print(cities[index])'''


'''list = [] #This is a list from 1 to 1000 that prints only the even numbers.
for number in range(1, 1000, 2):
    list.append(number + 1)
print(list)'''


'''
list = []
number = int(input("Hello please enter an number: "))
while number >= 3 and number <=20:
    list.append(number)
    list.sort()
    print(list)
    number = int(input("Hello please another number: "))'''


def main():
    print(" Welcome to the email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension: ", extension)


while True:
    main()
