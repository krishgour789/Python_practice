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

# n = int(input("enter a number : "))
# for i in range(2,n):
#     if n%i==0:
#         print("Not Prime Number")
#         break

# else:
#     print("prime")
# li = [12,23,54,23,56]
# index = 3
# new_li = []
# for i in range(len(li)):
#     if index!=i:
#         new_li.append(li[i])
# print(new_li)


# li = [12,23,54,23,56]
# n = 23
# new_li = []
# for i in li:
#     if i!=n:
#         new_li.append(i)
# print(new_li)


# lst = [10, 20, 30, 40, 50]
# item_to_remove = 30

# new_list = []
# for x in lst:
#     if x != item_to_remove:
#         new_list.append(x)

# print(new_list)  


# li = [1,2,3,3,34]
# remove = 2
# new = []
# for i in li:
#     if i != remove:
#         new.append(i)

# print(new)


## remove duplicate



'''li =  [1, 2, 2, 3, 4, 4]
dup = {}
new = []
for i in li:
    if i not in dup:
        dup[i] = True
        new.append(i)
print(new)
'''


# to reverse a number
'''l = [1,2,3,4,5]
i = 0
last = len(l)-1 
while i<last:
    l[i],l[last] = l[last],l[i]

    i+=1
    last-=1
print(l)'''

# list = [1,1,2,2,3,4,5,5]
# freq = {}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i] = 1
# print(freq)

# start = 1
# end = 50
# for num in range(start,end+1):
#     if num>1:
#         is_prime = True
#         for i in range(2,num):
#             if num%i==0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num,end=' ')
# start = 1
# end = 50

# for num in range(start, end + 1):
#     if num > 1:  # prime numbers are > 1
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)

# l = [1,2,3,4,5,6,7,7,7]
# count = 0
# for i in l:
#     if i%2!=0:
#         count+=1
# print(count)

# l = [1,2,3,4,6,7]
# max = l[0]
# for i in l:
#     if i>max:
#         max = i

# print(max)

# l = 'kris'
# temp = l
# last = ''
# for i in l:
#     last = i+last
# print(last)

# n = int(input("Enter a number :"))
# a,b = 0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# n = 'Lrishkjskjfs'
# Vowel = 0
# Cons = 0
# a= 'AEIOUaeiou'
# for i in n:
#     if i in a:
#         Vowel+=1
#     else:
#         Cons+=1
# print(f"Vowels :{Vowel}, Const : {Cons} ")


# n = str(input("Enter a name :"))
# temp = n
# last = ''
# for i in n:
#     last = i+last
# print(last)
# if last==n:
#     print("Its Anagram")
# else:
#     print("Not anagram")

# str1 = "listen"
# str2 = "silent"

# if len(str1) != len(str2):
#     print("Not Anagram")
# else:
#     count1 = {}
#     count2 = {}

#     for char in str1:
#         count1[char] = count1.get(char, 0) + 1

#     for char in str2:
#         count2[char] = count2.get(char, 0) + 1
#     print(count1)
#     print(count2)
    # if count1 == count2:
    #     print("Anagram")
    # else:
    #     print("Not Anagram")


# l = [1,2,3,4,5,12,13,3]
# max = l[0]
# sec_max = l[0]
# for i in l:
#     if i>max:
#         sec_max = max
#         max = i
    
# print(sec_max)


# n = int(input("Enter a Number :"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
    
# else:
#     print("Prime Number")
# start = 0
# end = 50
# for i in range(start,end+1):
#     if i>1:
#         prime = True
#         for num in range(2,i):
#             if i%num==0:
#                 prime = False
#                 break
#         if prime:
#             print(i,end=' ')

# start = 0
# end = 50
# count = 0
# for i in range(start,end+1):
#     if i>1:
#         prime = True
#         for num in range(2,i):
#             if i%num==0:
                
#                 prime = False
                
#                 break
#         if prime:
#             print(i)
#             count+=1
# print(f"The Prime number between {start} and {end} is {count}")

# n = [1,2,4,5,6,7]
# sum = 0
# ni = len(n)
# for i in n :
#     sum+=i
#     n=  sum//ni
   
# print(n)

# n = [1,2,4,5,6,7]

l = [1,2,2,3,4,55,5,4,]
# unique = []
# for i in l:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# n = "hello krish"

# new = {}
# for i in n:
#     if i !='':
#         if i in new:
#             new[i]+=1
#         else:
#             new[i] = 1
# print(new)

# n = int(input("Enter a number"))
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

a = 'kroish 222'
l = 0
s = 0
d = 0
for i in a :
    if i.isalpha():
        l+=1
    elif i.isspace():
        s+=1
    elif i.isdigit():
        d+=1
print("Letter :",l)
print("space :",s)
print("digit :",d)

