with open("flag.txt") as f:
    text = f.readline()
l = len(text)
i = 0
flag = ""
while i+4 < l:
    while(text[i:i+4].lower() != "bonk"):
        flag += text[i]
        i += 1
    i += 4
print(flag)