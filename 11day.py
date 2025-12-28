# print("5"*3)
# print("5"+"3")

# s1 = 'Neeraj'
# s2 = 'Neraj'
# print(s1>s2)

# def length_string(s):
#     count=0
#     for i in s:
#         count+=1
#     return count
# print(length_string("krish"))

# def count_char(s,target):
#     count=0
#     for char in s:
#         if char==target:
#             count+=1
#     return count
# a = count_char("kriiish","i")
# print(a)

# def reversed_s(s):
#     s1 = ''
#     for i in range(s-1,-1,-1):
#         s1 += s[i]
#     return s1
# print(reversed_s("krish"))


# def is_palindrome(s):
#     n = len(s)
#     for i in range(n//2):
#         if s[i]!=s[n-1-i]:
#             return False
#     return True
# print(is_palindrome("ala"))

# def to_lower_case(s):
#     result = '' 
#     for i in s:
#         if 'A'<= i <= 'Z':
#             result+=chr(ord(i)+32)
#         else:
#             result+=i
#     return result
# print(to_lower_case("KRISH"))


# def to_upper_case(s):
#     result = '' 
#     for i in s:
#         if 'a'<= i <= 'z':
#             result+=chr(ord(i)-32)
#         else:
#             result+=i
#     return result
# print(to_upper_case("krish"))


# def remove_space(s):
#     result = ''
#     for i in s:
#         if i!=' ':
#             result+=i
#     return result
# print(remove_space("Kir kk"))

# def remove_space(s):
#     result = ''
#     for i in s:
#         if....?

# def count_word(s):
#     count = 0
#     is_word = False
#     for i in s:
#         if i!=' ' and not is_word:
#             count+=1
#             is_word = True
#         elif i==' ':
#             is_word = False
#     return count
# s = count_word(" us saa a")
# print(s)


# def replace_word(s,old,new):
#     result = ''
#     for i in s:
#         if i == old:
#             result+=new
#         else:
#             result+=i
#     return result
# print(replace_word("Krish",'s','i'))  
# 

      


        
# def count_words(s):
#     count = 0
#     in_word = False
#     for ch in s:
#         if ch != ' ' and not in_word:
#             count += 1
#             in_word = True
#         elif ch == ' ':
#             in_word = False
#     return count
# print(count_words('krikk j hghghg'))









s1 = "Neeraj"
s2 = "Neraj"
print(s1>s2)