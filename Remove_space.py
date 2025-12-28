def remove_space(s):
    result = ''
    for i in s:
        if i!=" ":
            result+=i
    return result
print(remove_space("Krish Gour"))