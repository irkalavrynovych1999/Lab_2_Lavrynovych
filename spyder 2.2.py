c = int(input('Введіть кількість стовпців: '))
r = int(input('Введіть кількість рядків: '))
nums = input('Введіть {} елементів через кому: '.format(c*r)).split()

if c*r != len(nums):
    print('Було введено {}, а треба {}'.format(len(nums), c*r))
    exit(0)

dv_spisok = []
iterator = 0

for i in range(r):
    s = []
    for j in range(c):
        s.append(nums[iterator])
        iterator += 1
    dv_spisok.append(s)

print('Масив: ({}x{})'.format(r, c))
for s in dv_spisok:
    print(' '.join(s))

a = []
b = []
upper_part = r // 2


for i in range(upper_part):
    a.append(dv_spisok[i])

if r%2 != 0:
    upper_part += 1

for i in range(upper_part, r):
    b.append(dv_spisok[i])

print(a)
print(b)
if a == b:
    print('Список горизонтально симетричний')
else:
    print('Список горизонтально не симетричний')

