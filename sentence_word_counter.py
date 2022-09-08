line = map(str, input("Enter a sentence:").split())
sentence = []
dic = {}
for i in line:
    i = i.lower()
    sentence.append(i)
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

biggest = {}

for key in dic:
    if dic[key] == max(dic.values()):
        biggest[key] = max(dic.values())

words = []
for i in biggest.keys():
    words += [i]

word = words.sort()

print("Most used word is " + words[0])