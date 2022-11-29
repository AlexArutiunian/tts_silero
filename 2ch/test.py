word=input()
test=open(f'{word}.txt', 'w')
test.write(f'No text. This is file {word}.txt')
test.close()