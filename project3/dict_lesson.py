#excersice one
'''dict = {
    "itamos" :  "proklitikos ,aufthadis ,anaidis",
    "oneidos" : "kataisxini",
    "pomfoliges" : "anoisies, anoisies"
}
print(dict) # print the dictionary
dict["flinafimata"] = "anoisies, saxlamares" # add a new key flinafimata with the value of anoisies and saxlamares
print(dict)

key = input("Dwse tin leksi ")
value = input("Dwse tin epeksigisi  ")

dict[key] = value
print(dict)'''

'''service  = {
    "name" : " ",
    "surname" : "",
    "Father's name" : "",
    "date of birth" : "",
    "adress" : "",
    "phone" : "",
}
print(service)
service["name"] = "Dimitrios"
service["surname"] = "Karakostas"
service["Father's name"] = "Xristos"
service["date of birth"] = "17/04/1996"
service["adress"] ="Riga Ferraiou 2"
service["phone"] = "6987551056"'''

"""hero = {"name" : "Tony Stark", "alias" : "Ironman"}
for key in hero:
    print(key)
for key,value in hero.items():
    print(key + " is " + value)
for key in hero.keys():
    print(key)"""
'''from random import randrange
dict = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0
}
i = 0
for i in range(10000000):
    rand = randrange(1,7)
    dict[rand] += 1
print(dict)

for i in range(1,6+1):
    print(str(i) + ": " + str(dict[i]/1000000))'''

