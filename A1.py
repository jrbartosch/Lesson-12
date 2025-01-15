word = input ('Please Enter a Word: ')
char = input ('Please Enter a Character to Count in the Word: ')
i = 0
count = 0
while (i < len(word)):
    if (word[i] == char):
        count += 1
    i += 1
print (char, 'repeats', count, 'times in this word.')