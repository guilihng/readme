
x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
xxx = 0
yyy = 0
a1 = 0
a2 = 0
for i in range(len(x)):
    xxx += x[i]
    
pingjunx = xxx / len(x)

for j in range(len(y)):
    yyy / len(y)
    
pingjuny = yyy / len(y)

for i in range(10):
    a1 += (x[i] - pingjunx) * (y[i] -pingjuny)
    a2 += (x[i] - pingjunx) * (x[i] - pingjunx)
    
w = a1/ a2
print(w)
b = pingjuny - w * pingjunx
print(b)
