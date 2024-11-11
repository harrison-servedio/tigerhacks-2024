alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for _ in range(16):
    alph.insert(0, alph.pop())

s = input()

out = ""

for c in s:
    if c == " ":
        out += " "
        continue
    out += alph[ord(c)-65]

print(out)