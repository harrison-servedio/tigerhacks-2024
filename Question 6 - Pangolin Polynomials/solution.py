N = int(input())
coords = []
for i in range(N):
    line = list(map(int, input().split(" ")))
    coords.append((line[0], line[1]))

def shoelace_area(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to the first point at the end
        area += (x1 * y2) - (y1 * x2)

    return abs(area) / 2

print(int(shoelace_area(coords)+0.5))