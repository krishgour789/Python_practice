# Find the max without using max() ?
num = [1,2,3,4,5]
m = num[0]
for i in num:
    if i>m:
        m = i
print(m)