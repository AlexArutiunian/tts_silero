def replace_word(fname, before, after):
    with open(fname, 'r', encoding="utf-8") as file :
        filedata = file.read()        
    filedata = filedata.replace(before, after)  
    with open(fname, 'w', encoding="utf-8") as file:
        file.write(filedata)
for i in range(15,125):
    replace_word(f'rus_text/{i}.txt', 'RUS_TEXT:', ' ')
    replace_word(f'rus_text/{i}.txt', 'ENG_TEXT:', ' ')
    replace_word(f'rus_text/{i}.txt', 'Поттенгер', 'Поттенджер')