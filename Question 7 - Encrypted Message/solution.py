n = int(input())

instructions = [">", "<", "+", "-", "."]
in_dict = {}
for i in instructions:
    in_dict[ord(i)] = i

commands = []

for _ in range(n):
    base, num = input().split(":")
    commands += [in_dict[int(num, int(base))]]

cells = [0] * 10
pointer = 0
for c in commands:
    if c == "+":
        cells[pointer] += 1
    elif c == "-":
        cells[pointer] += -1
    elif c == ">":
        pointer += 1
    elif c == "<":
        pointer += -1
    elif c == ".":
        print(chr(cells[pointer]), end="")
