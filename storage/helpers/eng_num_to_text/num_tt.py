from num2words import num2words as nn
import os
def number_in_english(n):
    return nn(n)
def file_num_num():    
    with open('eng_num_to_text/num_num.txt', 'w', encoding='utf-8') as f:
        for i in range(0, 3000):
            f.write(f'{i}')
            f.write('\n')
def file_word_num():
    with open('eng_num_to_text/word_num.txt', 'w', encoding='utf-8') as f:
        for i in range(0, 3000):
            f.write(nn(i))
            f.write('\n')
def replace_word(fname, before, after):
    with open(fname, 'r', encoding="utf-8") as file :
        filedata = file.read()        
    filedata = filedata.replace(before, after)  
    with open(fname, 'w', encoding="utf-8") as file:
        file.write(filedata) 

def add_plus_and_textnum(fname):
    lst1 = []
    lst2 = []
    dump_strfile_in_lst('eng_num_to_text/num_num.txt', lst1)
    dump_strfile_in_lst('eng_num_to_text/word_num.txt', lst2)               
    for elem1, elem2 in zip(lst1, lst2):
        replace_word(fname, f" {elem1} ", f" {elem2} ") 

def dump_strfile_in_lst(filename, lst):
    filename = os.path.abspath(filename)
    with open(f'{filename}', 'r', encoding="utf-8") as file:
        for line in file:
            lst.append(line.rstrip()) 
                   