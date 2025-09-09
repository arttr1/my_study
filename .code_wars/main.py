# import re

# s = (input('/// '))
# # for i in range(1, len(s)):

# a = re.split('[-_]', s)
# for i in range(1, len(a)):
#     if len(a[i])==0: continue
    
#     ch = a[i][0].upper()
#     a[i] = ch + a[i][1:]
    
# for i in a:
#     print(i, end='')
c = input('___')
def to_camel_case(text):
    
#     a = re.split('[-_]', text)
#     for i in range(1, len(a)):
#         if len(a[i])==0: continue

#         ch = a[i][0].upper()
#         a[i] = ch + a[i][1:]
#     s = ''
#     for i in a:
#         s+=i
    s = ''
    for i in range(1, len(text)):
        if text[i-1]=='_' or text[i-1]=='-': 
            ch = text[i].upper()
            s = text[:i-1] + ch + text[i+1:]
            return to_camel_case(s)
    return s
print(to_camel_case(c))