# s = input()

# count = 1
# compressed = []
# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count+=1
#     else:
#         compressed.append(s[i-1] + str(count))
#         count = 1

# compressed.append(s[len(s) - 1]+str(count))
# ans = ''
# for i in compressed:
#     ans += i

# print(ans) 