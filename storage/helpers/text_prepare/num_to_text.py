name_of_numbers = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь',
                   'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
                   'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                   'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать']
ten_numbers = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
               'семьдесят', 'восемьдесят', 'девяносто']
 
 
def number_to_words(n):
    if n <= 20:
        return name_of_numbers[n - 1]
    else:
        ten = int(str(n)[0])
        if str(n)[1] != '0':
            num = int(str(n)[1])
            str1 = ' '.join([ten_numbers[ten - 2], name_of_numbers[num - 1]])
            return str1
        else:
            return ten_numbers[ten - 2]
if __name__ == '__main__':
    EMPTY = ''
 
    
    with open('num.txt', 'w') as file:
        for i in range(200):
            file.write(str(i + 1))
            file.write('\n')
    with open('num_.txt', 'w', encoding="utf-8") as file:
        for i in range(100):
            file.write('стo ')
            file.write(number_to_words(i + 1))
            file.write('\n')
    