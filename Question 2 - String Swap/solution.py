n = int(input().split(" ")[1])

word = list(input())

for i in range(n):
    i, j = input().split(" ")
    i, j = int(i), int(j)

    word[i], word[j] = word[j], word[i]

print("".join(word))