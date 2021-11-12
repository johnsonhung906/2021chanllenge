#!/usr/bin/env python3
from random import randint

# print author, commit words
authors = [
    "John Doe <john@dd.org>", 
    "Oscar <oscar@dd.org>", 
    "Johnson <johnson@dd.org>", 
    "Jeffery <jeffery@dd.org>",
    "Kevin <kevin@dd.org>", 
    "Alex <alex@dd.org>", 
    "Tom <tom@dd.org>"
]

num_a = randint(0, len(authors)-1)

print(authors[num_a])
