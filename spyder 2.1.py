n = input('Введіть числа (мінімум 5 елементів):')

nums = n.split()
int_nums = []

for n in nums:
    int_nums.append(int(n))

int_nums.sort()

suma = 0

print(int_nums[-5:])

for i in int_nums[-5:]:
    suma += abs(i*i*i)

print('Сума кубів 5 найбільших елементів: ', suma)