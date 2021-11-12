#!/usr/bin/env python3
from random import randint

# txt changed
trash_talks = [
    "If he calls that number, I'll be sure to pick up after the fifth ring.", 
    "I’m just looking around to see who’s gonna finish second.",
    "Fatso there just forgot to shake my hand, I guess.",
    "Loat like a butterfly and sting like a bee...his hands can't hit what his eyes can't see.",
    "I'll call the President. President, we need the National Guard! We need as many men as you can spare! Because we are killing the Patriots! So call the dogs off! Send the National Guard, please!",
    "fo', fo', fo.",
    "Aftzxer the fight I'm gonna build myself a pretty home and use him as a bearskin rug. Liston even smells like a bear. I'm gonna give him to the local zoo after I whup him.",
    "If he calls that number, I'll be sure to pick up after the fifth ring. ", 
    "I’mx just looking around to see who’s gonna finish second. ",
    "Fatso there just forgot to shake my hand, I guess. ",
    "Loat like a butterfly and sting like a bee...his hands can't hit what his eyes can't see. ",
    "I'll call the President. President, we need the National Guard! We need as many men as you can spare! Because we are killing the Patriots! So call the dogs off! Send the National Guard, please! ",
    "fo', fo', fo. ",
    "After the fight I'm gonna build myself a pretty home and use him as a bearskin rug. Liston even smells like a bear. I'm gonna give him to the local zoo after I whup him. "
]

f = open('trash_words.txt','r')
trash_l = f.readline()
num = randint(0, len(trash_talks)-1)

# while(trash_talks[num] == trash_l):
#     num = randint(0, len(trash_talks)-1)
    
print(trash_talks[num]+randint(0, 1000)*' ')
