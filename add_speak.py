
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
