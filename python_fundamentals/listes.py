#askisi me lista vres ton megisto simple
"""numbers = [3, 5, 7]
max = numbers[0]
if numbers[1] > max:
    max = numbers[1]

if numbers[2] > max:
    max = numbers[2]
print(max)"""

"""
numbers = [1, 65, 32, 87, 433]
print(numbers[1:])#The output is from the second element of the list until the end
print(numbers[:2])#The output is from the first element of the list until the second
# number list[: index - 1] for example.
"""

"""Mesos oros apo tous 2 prwtous arithmous
ekloges = [55, 28, 20]
print((ekloges[0] + ekloges[1]) / 2)"""

# The list is a class and it has many methods like .append() which is a method that input an element in the last at the end of the list
numbers = [1, 3, 6, 8,]
numbers.append(2) # the 2 element is implemented at the end of the list
print(numbers)

numbers.insert(1, 4)# the insert method put the element 4 at the position of 1 in the list
print(numbers)

numbers.extend([1, 3])# extends the list
print(numbers)

numbers.pop(4)
print(numbers)# deletes the number at the position 4 of the list
# but if you dont a attribute inside the pop() by default it removes the last element
numbers.pop()
print(numbers)

numbers.remove(2)# the remove method removes the ELEMENT that is inside the list like the example
print(numbers)

numbers.clear()#removes all the Elements from the list.
print(numbers)

#askisi
"""stack = []
stack.append("Bob")
stack.append("john")
print(stack)
person = stack.pop()
print(person + " servered.")
stack.append("Pat")
print(stack)"""

numbers = [1, 34, 56, 4, 38]
numbers.sort()#Sort the elements of the list in ascending order
print(numbers)

numbers.reverse()# the reverse() method that reverse all the elements of the list
print(numbers)
'''##askisi me listes4 psounis
list = []
number = float(input("Please insert the first number: "))
list.append(number)

number = float(input("Please insert the second number: "))
list.append(number)
number = float(input("Please insert the third number: "))
list.append(number)
list.sort()
print(list)'''

'''exercise 2
movies = ["Avengers", "The eternal sunshine of a spotless mind", "Closer", "Usual Suspects"]
fav_movie=input("Please add your favourite movie: ")

if fav_movie in movies:
        print("Not saved, already exists")
else:
    movies.append(fav_movie)
    movies.sort()
    print(movies)
    print(len(movies))'''