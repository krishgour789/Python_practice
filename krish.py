
# ----------------------------Program to check if a number is a palindrome
'''num = int(input("Enter a Number"))
temp= num
rev = 0
while temp!=0:
    digit = temp %10
    rev = rev*10+digit
    temp = temp//10
if rev==num:
    print("Pallidrome")
else:
    print("Not Pallidrome")'''


#----------------------to check if a number is a a reverse----------------------
'''num = int(input("Enter a Number"))
temp= num
rev = 0
while temp!=0:
    digit = temp %10
    rev = rev*10+digit
    temp = temp//10
print(rev)
'''


# -------------TO COunt the Vowels---------------
'''n = str(input("Enter a words"))
a = 'aeiouAEIOU'
Vowels = 0
for i in n:
    if i in a:
        Vowels+=1
print(Vowels)'''


# n = str(input("Enter a words"))
# a = 'aeiouAEIOU'
# Vowels = []
# for i in n:
#     if i in a:
#         Vowels.append(i)
# print(Vowels)

# li = ['Python','Java','PHP']
# print(li[1][-1])


'''li = {"name":"Krish Gour",
      "age":21,
      "city":"Sehore"}
for key,value in li.items():
    print(key,":",value)'''

num = [10,20,8,25,25]
largest = 0
very_largest = 0
for i in num:
    if i>largest:
        largest = very_largest
        very_largest = i
        print(very_largest)
    


        