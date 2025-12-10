# n = int(input("Enter a name :"))
# l = len(str(n))
# print(l)

n = int(input("Enter a number : "))
temp = n
rev = 0
total = len(str(n))
while temp!=0:
    digit = temp%10
    rev = rev+(digit**total)
    temp //=10
if rev == n:
    print(f"{n} is Armstrong Number ")
else:
    print(f"{n} is not Armstrong Number")