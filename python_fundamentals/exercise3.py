'''i = 0
list = []
new_list1 = ()
while i < 10:
    user_input = int(input("Please enter a number: "))
    list.append(user_input)
    i += 1
new_list = tuple(list[:])
print(new_list)'''

 # Exercise with the print tree
'''N = 5
for i in range(N):
    print(" " * (N-i-1), end="")
    print("*" * (2*i+1), end="")
    print("")'''

'''N = 7

if N == 0 or N == 1:
    print("The number is not prime")
else:
    for i in range(2, N):
        if N % i == 0:
            print("It is not prime")
            break
    else:
        print("Its a prime number")'''


'''N = 100
list = []
for N in range(2, 100+1):
    for i in range(2, N):
        if N % i == 0:
            break
        else:
        list.append(N)

primes_list = tuple(list)
print(primes_list)'''

#list comrehensions
'''list = []
list = [number for number in range(7)]
list1 = [number for number in range(7) if number > 5]
list_2 = [number if number > 3 else number * 2 for number in range(9)]
print(list1, list_2)'''

''' makes a list that contains even numbers and are devided by 3 
list = []
list = [number for number in range(100) if number % 2 == 0 and number % 3 == 0]
print(list)'''

#create a 2D list
'''array = []
rows = int(input("Give a number of rows: "))
columns = int(input("Give a number of columns: "))

for i in range(rows):
    array.append([])
    for j in range(columns):
        elem = int(input("Give " + str(i) + " , " + str(j) + " element: "))
        array[i].append(elem)
print(array)'''

'''array = [
    [1,2,4,5],
    [5,6,7,8],
    [8,9,1,2]
]
array.insert(0, [0,0,0,0])
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")
for row in array:
    row.append(1)
    
for row in array:
    for elem in row:
        print(elem, end=" ")
    print("")'''






