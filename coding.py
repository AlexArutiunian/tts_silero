codecs = ["cp1252", "cp437", "utf-16be", "utf-16"]

file = open("test_file.txt", "r", encoding="utf-8")
text = file.read()
print(text)