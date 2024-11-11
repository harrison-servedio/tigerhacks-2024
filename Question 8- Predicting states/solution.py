a = float(input())
input()
c = float(input())
input()

x1 = 1/(1+(1/c)-(a/c))
x2 = (x1/c)-(a*x1/c)

x1 = round(x1*10**6)/10**6
x2 = round(x2*10**6)/10**6
print(f"{x1} {x2}")