f = open("2ch.txt", "r")
i = 1
j = 1

while(i != 5):
    j = 1
    while(j != 4):
        res = open(f'text/{i}_{j}.txt', "w")
        for k in range(1000):
            c = f.read(1)    
            if((k > 850) * (c == '.')):
                res.write(c)
                break
            else:
                if(((k % 75) == 0)):
                    res.write('\n')
                res.write(c)
        j += 1
    i += 1            