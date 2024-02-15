'''
syntax errors and logic erros:
syntax errors pheraps you forgot a komma or a dot or you didnt close the brackets
logic errors: when you the syntax of the programm is correct but the program that you have made gave a weird result
you cannot see logic errors
for example below:
'''

s = 0
for i in range(1,100 + 1):
    s += 1//i
print(s)
# That is a logic error
s = 0
for i in range(1,100):
    s += 1//i
    print(" i=" + str(i)+ " 1/i=" + str(1/i) + " s=" + str(s))

