# задание 1

# Трушин Артём
# ' f4 d2 d5 db c9 ce 9a e1 d2 d4 a3 cd' in koi8-r
# ' d2 f0 f3 f8 e8 ed 20 c0 f0 f2 b8 ec' in win-1251
# 1058 1088 1091 1096 1080 1085 32 1040 1088 1090 1105 1084 in utf-16

# 9a - space in koi8-r
# 20 - space in win-1251

# c = 'Трушин Артём'
# a0 = c.encode('koi8-r')
# a = c.encode('windows-1251')
# print(a0)
# print(a)
# for i in c:
#     print(ord(i), end=' ')

# a = input().split()
# for i in a:
#     print(hex(int(i))[2:], end=' ')


# ------------------------------------------------------------
# задание 2
# Среда разработки 
#  91 e0 a5 a4 a0 20 e0 a0 a7 e0 a0 a1 ae e2 aa a8 - cp866
#  f3 d2 c5 c4 c1 9a d2 c1 da d2 c1 c2 cf d4 cb c9 - koi8-r

#Конфигурация 
#  8a ae ad e4 a8 a3 e3 e0 a0 e6 a8 ef - cp866
#  eb cf ce c6 c9 c7 d5 d2 c1 c3 c9 d1 - koi8-r

# s = 'Среда разработки'

# a = s.encode('koi8-r')
# print(a)
# ------------------------------------------------------------
# задание 3
#  88 ad e4 ae e0 ac a0 e2 a8 aa a0 - Информатика
# 50 72 6f 67 72 61 6d - Program
# 43 6f 6d 70 75 74 65 72 20 49 42 4d 20 50 43 - Computer IBM PC


# s1 = b'\x88\xad\xe4\xae\xe0\xac\xa0\xe2\xa8\xaa\xa0'
# s2 = b'\x50\x72\x6f\x67\x72\x61\x6d'
# s3 = b'\x43\x6f\x6d\x70\x75\x74\x65\x72\x20\x49\x42\x4d\x20\x50\x43'
# a1 = s1.decode('cp866')
# a2 = s2.decode('cp866')
# a3 = s3.decode('cp866')
# print(a1)
# print(a2)
# print(a3)
# # ----------------------------------------------------------

#задание 4

# 145 170 174 224 174 255 170 160 173 168 170 227 171 235 - Скоро каникулы
# s = '145 170 174 224 174 255 170 160 173 168 170 227 171 235' 
# a = s.split()
# a_hex = []
# for i in a:
#     a_hex.append(hex(int(i))[2:])
# st = b'\x91\xaa\xae\xe0\xae\xff\xaa\xa0\xad\xa8\xaa\xe3\xab\xeb'
# print(st.decode('cp866'))


c ='de c5 d4 d9 d2 c5 9a  d0 d1 d4 d8'.split()
for i in c:
    print(bin(int(i, 16))[2:], end=' ')

# c = 'четыре пять'
# # for i in c:
# #     print(hex(ord(i))[2:], end=' ')
# print(c.encode('win-1251'))