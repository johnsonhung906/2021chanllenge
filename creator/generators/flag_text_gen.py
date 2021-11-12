import random

flag = "FLAG{7RaSH_7a1k}"
words = ["bonk", "BonK", "bONk", "BoNK"]
output = ""
flag_len = len(flag)
ptr = 0
p = 0.01

while ptr < flag_len:
    if random.random() < p:
        output += flag[ptr]
        ptr += 1
    word = words[random.randint(0,len(words)-1)]
    output += word

print(output)