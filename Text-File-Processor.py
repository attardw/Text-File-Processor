import matplotlib.pyplot as plt
import re
filename = "Frankenstein.txt"
word_count = {}

with open(filename, 'r') as file:
    for line in file:
        wordsInLine = line.split(" ")
        for word in wordsInLine:
            word = re.sub(r'[^\w\']', '', word)
            if len(word)!=0:
                if word in word_count.keys():
                    word_count[word] += 1
                else:
                    word_count[word] = 1

sorted_dict = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}

print("Word used most: " )
print(list(sorted_dict.keys())[0], ":", sorted_dict[list(sorted_dict.keys())[0]] )
print("Longest word:")
print(max(list(sorted_dict.keys()), key=len))

wordsInLine = list(sorted_dict.keys())[:50]
freq = [sorted_dict[wordsInLine[i]] for i in range(50)]
fig, ax = plt.subplots(figsize=(10,10))

plt.bar(range(len(wordsInLine)), freq, align='center')
plt.xticks(range(len(wordsInLine)), wordsInLine, rotation=90)
plt.yticks(rotation=90)
plt.xlabel("Word")
plt.ylabel("Frequency")

for bar in ax.patches:
    text = str(bar.get_height())
    text_x = bar.get_x()
    text_y = bar.get_y() + bar.get_height()
    ax.text(text_x, text_y, text, rotation="vertical")

plt.show()

wordsInLine = list(word_count.keys())
wordsInLine = sorted(wordsInLine, key=len, reverse=True)

longest_words = wordsInLine[:50]
longest_words = sorted(longest_words, key=len)

freq = [word_count[longest_words[i]] for i in range(50)]

fig, ax = plt.subplots(figsize=(10,10))
plt.bar(range(len(longest_words)), freq, align='center')
plt.xticks(range(len(longest_words)), longest_words, rotation=90)
plt.yticks(rotation=90)
plt.xlabel("Word")
plt.ylabel("Frequency")

plt.show()