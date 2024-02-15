'''string = "Today the weather in Utrecht was rainy, and also it was very cold outside"
print(string)
my_list = list(string)
print(my_list)

dictionary = {}
for char in my_list:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1

print(dictionary)
max = (max(list(dictionary.values())))# finding the max number from dictionary
for key,value in dictionary.items():
    print(str(key) + " " + str(value) + " " + str(max))
    if value == max:
        print(key)'''

'''dict1 = {v:v**2 for v in range(10)}
print(dict1) # dict comprehensions

merchandise = {
    "book": 10.18,
    "parsley": 0.22,
    "cement": 5.17,
    "CD": 0.05
}
rate = 2.3
new_values = {key: value*rate for key,value in merchandise.items()}
print(new_values)'''

'''buildings = {
    "Burj Khalifa": "United Arab Emirates",
    "Shanghai Tower": "China",
    "Abraj Al-Bait Clock Tower": "Saudi Arabia",
    "Ping An Finance Center": "China",
    "Lotte World Tower": "South Korea",
    "One World Trade Center": "United States",
    "Guangzhou CTF Finance Center": "China",
    "Tianjin CTF Finance Center": "China",
    "Zun Taipei": "Taiwan",
    "Shanghai World Financial Center": "China",
    "Central Park Tower": "United States",
    "Lakhta Center": "Russia",
    "Landmark": "Vietnam",
    "Changsha IFS Tower": "China",
    "Petronas Tower 1": "Malaysia",
    "Petronas Tower 2": "Malaysia",
    "Zifeng Tower": "China",
    "Suzhou IFS": "China",
    "The Exchange": "Malaysia",
    "Willis Tower": "United States",
    "KK100": "China",
    "Guangzhou International Finance Center": "China",
    "Wuhan Center": "China",
    "111 West 57th Street": "United States",
    "One Vanderbilt": "United States",
    "Dongguan International Trade Center": "China",
    "432 Park Avenue": "United States",
    "Marina 101": "United Arab Emirates",
    "Trump International Hotel and Tower": "United States",
    "Jin Mao Tower": "China",
    "Princess Tower": "United Arab Emirates",
    "Al Hamra Tower": "Kuwait",
    "International Finance Centre": "China",
    "Haeundae LCT The Sharp Landmark Tower": "South Korea",
    "Nanning China Resources Tower": "China",
    "Guiyang Financial Center Tower": "China",
    "China Resources Headquarters": "China",
    "23 Marina": "United Arab Emirates",
    "Shun Hing Square": "China",
    "Eton Place Dalian Tower 1": "China"
}

country_buildings = {}
for key,value in buildings.items():
    if value not in country_buildings:
        country_buildings[value] = [key]
    else:
        country_buildings[value].append(key)
print(country_buildings)'''

'''family = {
    "father": {
        "name": "Homer Simpson",
        "occupation": "nuclear safety inspector",
        "quotes": [
            "Lord Help Me, I’m Just Not That Bright",
            "Kids, You Tried Your Best And You Failed Miserably. The Lesson Is, Never Try.",
            "It Takes Two To Lie; One To Lie, And One To Listen.",
            "To Alcohol! The Cause Of, And Solution To, All Of Life's Problems.",
            "I Am So Smart! I Am So Smart! S-M-R-T! I Mean S-M-A-R-T!",
            "D'Oh!"
        ]
    },
    "mother": {
        "name": "Marge Simpson",
        "occupation": "housewife",
        "quotes": [
            "Am I Pregnant?",
            "And all this time I thought 'Googling yourself' meant the other thing.",
            "Homer, we have to do something. Today he's drinking people's blood. Tomorrow he could be smoking.",
            "I guess one person can make a difference. But most of the time, they probably shouldn't."
        ]
    },
    "children": [
        {
            "name": "Bart Simpson",
            "quotes": [
                "Eat My Shorts!",
                "I'm Bart Simpson, who the hell are you?",
                "You got the brains and talent to go as far as you want and when you do I'll be right there to borrow money"
            ]
        },
        {
            "name": "Lisa Simpson",
            "quotes": [
                "Does It Make You Feel Superior To Tear Down People’s Dreams?",
                "Pablo Neruda Said, 'Laughter Is The Language Of The Soul.'",
                "I Just Think It's A Fantasy. If You Believe In Angels, Why Not Sea Monsters, Unicorns Or Leprechauns?"
            ]
        },
        {
            "name": "Maggie Simpson",
            "quotes": [
                "(sucking noise)",
                "(crying)",
                "Daddy!"
            ]
        }
    ]
}
#ti katalavaineis apo to papano leksiko?
#there is one dictionary name family with 3 keys father,mother,children, in those keys the values have an another dictionary
#with the keys of name, occupation and quotes which the quotes are a list

print(family["father"]["name"], ":")
print(family["mother"]["name"],":")
i = 0
while i<=2:
    print(family["children"][i]["name"])
    i += 1'''
