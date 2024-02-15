cards = [1,2,3,4,1,2,3,4]
N = 8

state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]
#temp open, open

active = True

while active:
    user_input = int(input("Please choose your first card: "))
    while (user_input < 0 or user_input >= N) or state[user_input] == "open":
        print("Error!")
        user_input = int(input("Please choose your first card: "))

    user_input2 = int(input("Please choose your second card: "))
    while (user_input2 < 0 or user_input2 >= N) or state[user_input2] == "open":
        print("Error!")
        user_input2 = int(input("Please choose your first card: "))
    state[user_input] = "temp_open"
    state[user_input2] = "temp_open"

    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(cards[position], end="")
        else: # temp open
            print(cards[position], end="")

    if cards[user_input] == cards[user_input2]:
        state[user_input] = "open"
        state[user_input2] = "open"
    else:
        state[user_input] = "closed"
        state[user_input2] = "closed"


active = False
