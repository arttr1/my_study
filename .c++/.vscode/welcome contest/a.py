def cnt(s):
    r = len(s)
    k = r//2

    # if len(s)%2 == 0:
    for i in range (k):
        if s[i] == s[r - 1 - i]:
            k-=1
    # else:
    return k

def pal(s):
    r = len(s)
    for i in range (r//2):
        if s[i] != s[r - 1 - i]:
            s[r - 1 - i] = s[i]
            print(s)



arr = []
# t = int(input())
# for i in range(t):
#     arr[i] = input()
s = 'Kirill'
print(cnt(s))
print(pal(s))