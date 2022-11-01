x = 3564
y=[]

while (x>0):
    y.append(x%10)
    x = x //10

y.sort()
x=0

for i in range(len(y)):
    x+= y[i]*10**i

print(x)