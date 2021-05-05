introstring = input("Enter your introduction: ")
wordcount = 1
charcount = 0

for i in introstring:
    charcount = charcount + 1
    if(i == ' '):
        wordcount = wordcount + 1

print("Number of word(s) in the string: ")
print(wordcount)
print("Number of characters(s) in the string: ")
print(charcount)