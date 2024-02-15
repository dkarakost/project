'''A = {1,2,3,4}
B = {4,6,7,8}
print("union" + str(A | B)) # units two sets together
print("Intersect: " + str(A & B)) # which element have in common
print("diff A - B: " + str(A - B)) # deletes the elements that have in common A
print("diff B - A: " + str(B - A)) # delete the elements that have in common from B'''

'''N = 100

evens = set() # add the even numbers
for number in range(0, N+1, 2):
    evens.add(number)
print(evens)

odd = set() # add the odd numbers
for number in range(1, N+1, 2):
    odd.add(number)
print(odd)

multiplies3 = set()
for number in range(0, N, 3):
        multiplies3.add(number)
print(multiplies3)''' # exercises with tuples

'''from random import randrange
from random import seed
N = 10

pupils = set()
for number in range(N):
    pupils.add("pupil" + str(number))
print(pupils)

# convert the pupils to list
list = list(pupils)
teams = set()
# repeat    N\2 list times
for _ in range (N//2):
    # pick a random positision, pop() this pupil
    pos1 = randrange(0 ,len(list))
    pupil1 = list.pop(pos1)
    pos2 = randrange(0, len(list))
    pupil2 = list.pop(pos2)
    team = (pupil2, pupil1)
    teams.add(team)
print(teams)'''



