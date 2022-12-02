f = open("6ch.txt", "r", encoding="utf-8")
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