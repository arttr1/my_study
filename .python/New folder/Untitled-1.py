row =  [' ', '|', ' ', '|', ' ']
row1 =  [' ', '|', ' ', '|', ' ']
row2 =  [' ', '|', ' ', '|', ' ']
row_ = ["========="]
table = [row, row_, row1, row_, row2]
for i in table: print(*i)
p = 0
while table[0].count('x')!=3 and table[4].count('x')!=3 and table[2].count('x')!=3:
    x, y = map(int, input().split())
    if p%2==0:
        table[y][x] = 'x'
        last = [x, y]
        
    else:
        table[y][x] = 'o'
    p+=1
    for i in table[::-1]: print(*i)
    print('=======================')
 

print(0)

