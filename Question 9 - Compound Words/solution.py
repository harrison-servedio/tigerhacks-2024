target = input()
n = int(input())

words = []
d = {}
for i in range(n):
    words.append(input())
    d[target.replace(words[-1], "")] = i

for i, word in enumerate(words):
    try:
        num = d[word]
    except:
        continue
    print(" ".join(sorted([str(num), str(i)])))
    break