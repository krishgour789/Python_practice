#______153 = Armstrong Number ________________________________
# n = int(input("Enter a number : "))
# temp = n
# rev = 0
# total = len(str(n))
# while temp!=0:
#     digit = temp%10
#     rev = rev+total**digit
# print(rev) 
# print(5**3)

# n = int(input("Enter a Number : "))
# sum=0
# for i in str(n):
#     sum+=int(i)
# print(sum)


# n = int(input("Enter a Number : "))
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b = b,a+b

# n = str(input("Enter a Name : "))
# temp = n
# last = ""
# for i in n:
#     last = i + last
# print(last)

n = int(input("enter a number : "))
for i in range(2,n):
    if n%i==0:
        print("Not Prime Number")
        break

else:
    print("prime")


        