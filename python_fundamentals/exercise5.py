'''from random import seed
from random import randrange
from datetime import datetime

seed(int(datetime.now().timestamp()))
for i in range(10):
    column = set()
    random_number = randrange(10, 20)

    column.add(random_number)
    while True:
        random_number = randrange(10,20)
        if random_number not in column:
            column.add(random_number)
            break

    # two numbers from 20 - 39

    random_number = randrange(20, 49)

    column.add(random_number)
    while True:
        random_number = randrange(20,49)
        if random_number not in column:
            column.add(random_number)
            break
    #1 - 9
    random_number = 2 * randrange(1,5)
    column.add(random_number)

    random_number = randrange(41, 50, 2)
    column.add(random_number)

    print(column)'''

