
f = open("6ch.txt", "r", encoding="utf-8") # поменять числа на числительные
i = 1
j = 1

while(i != 8):
    j = 1
    while(j != 4):
        res = open(f'text/text6/{i}_{j}.txt', "w", encoding="utf-8")
        for k in range(1000):
            c = f.read(1)    
            if((k > 850) * (c == '.')):
                res.write(c)
                break
            else:
                res.write(c)
                if((c == '.') + (c == ' ') * (k % 50 == 0)):
                    res.write('\n')
                    
                
        j += 1
    i += 1 
i = 1


while(i != 8):
    j = 1 
    while(j != 4):

        f = open(f'text/text6/{i}_{j}.txt', "a")
        f.write("</speak>")
        with open(f'text/text6/{i}_{j}.txt', "r+", encoding="utf-8") as fp:
            lines = fp.readlines()
            lines.insert(0, "<speak>")
            fp.seek(0)
            fp.writelines(lines)
        j += 1    
    i += 1            