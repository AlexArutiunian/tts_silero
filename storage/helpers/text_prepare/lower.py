import itertools
# Read in the file
with open('book.txt', 'r', encoding="utf-8") as file :
  filedata = file.read()

lst1 = []
lst2 = []

# Replace the target string
with open('alpA.txt', 'r', encoding="utf-8") as file:
    for line in file:
        lst1.append(line.rstrip())
with open('alp.txt', 'r', encoding="utf-8") as file:
    for line in file:
        lst2.append(line.rstrip())      
        
for elem1, elem2 in zip(lst1, lst2):
    print(f"{elem1}", f"{elem2}")

for elem1, elem2 in zip(lst1, lst2):
    filedata = filedata.replace(f"{elem1}", f"{elem2}")

# Write the file out again
with open('book.txt', 'w', encoding="utf-8") as file:
  file.write(filedata)