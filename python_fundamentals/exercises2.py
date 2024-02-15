'''for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print("")'''

'''friend = ["Tasos", "Xaris", "Giorgos"]
guests = []
for i in range(1,11):
    guest = input("Please enter the name of the guest ")
    guests.append(guest)
i = 0
j = 0
count = 0
for friend in guests:
    if friend in guests:
        count += 1
if count > 2:
    print("I must accept your beautiful invitation")
else:
    print("I must decline your beautiful invitation") '''


N = int(input("Please Enter a Number: "))
for i in range(0, N):
    for j in range(0, N-i-1):
        print(" ", end=" ")
    for j in range(0, 2*i + 1):
        print("*", end=" ")
    print("")



