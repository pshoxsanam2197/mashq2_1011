# 7
o = "shohsanam"
print(o)

uzunlik = len(o)
ortasi = uzunlik // 2
print("O'rtadagi harf: ", o[ortasi])

# 8
matn = input("Matn kirit: ")

if matn[0] == 'a' or matn[0] == 'A':
    print('YES')
else:
    print('NO')

# 9
count = 0
matn = "salom dunyo"
for i in range(len(matn)):
    if matn [i] == 'a':
        count +=1
print(count)

# 10
l = "salom dunyo"
print(l)
print(l[:: -1])
