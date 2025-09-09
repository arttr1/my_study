# a = 12345
# b = 54321
# c = a-b


# a_bin = bin(a)[2:]
# b_bin = bin(b)[2:]
# c_bin = bin(c)

# print(a_bin, len(a_bin))
# print(b_bin, len(b_bin))

# print(c_bin, len(c_bin))

# # '-0b1010001111111000'
# 1100000000000000

# print(bin(int('6b2d', 16))[2:])

a = input()
dis = ""
con = ""
def make_conjunction(row: int) -> str:
    return f"И(И(И({'X' if (row>>3)%2 else 'НЕ(X)'}, {'Y' if (row>>2)%2 else 'НЕ(Y)'}), {'Z' if (row>>1)%2 else'НЕ(Z)'}), {'W' if row%2 else 'НЕ(W)'})"

def make_disjunction(row: int) -> str:
    return f"ИЛИ(ИЛИ(ИЛИ({'X' if (row>>3)%2==0 else 'НЕ(X)'}, {'Y' if (row>>2)%2==0 else 'НЕ(Y)'}), {'Z' if (row>>1)%2==0 else 'НЕ(Z)'}), {'W' if row%2==0 else 'НЕ(W)'})"
for row in range(16):
    if a[row] == '1':
        dis = f"ИЛИ({dis}, {make_conjunction(row)})"
    elif a[row] == '0':
        con = f"И({con}, {make_disjunction(row)})"
    else:
        print('incorrect input!')
        exit()
# print(dis)
print('=========================================')
print(con)