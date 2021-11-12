#!/usr/bin/env python3
from random import randint

# print author, commit words

words = [
    "I am coding monster",
    "test for better sol",
    "please AC",
    "How stupid I am",
    "balo ha bong bong",
    "no pain no gain",
    "big test go go",
    "Do u want to build a snowman"
]

num_w = randint(0, len(words)-1)

print(words[num_w])