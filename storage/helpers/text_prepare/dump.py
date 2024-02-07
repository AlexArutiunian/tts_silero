import re
import codecs
fname = "book.txt"
with open(fname, "r", encoding="utf-8") as f:
    content = f.read()
    c = re.sub("[\'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]", "", content)

with open(fname, "w", encoding="utf-8") as f:
    f.write(c)
with open(fname, 'r', encoding="utf-8") as fileinput:
    for line in fileinput:
        line.rstrip().encode('utf-8').decode('utf-8').lower()  