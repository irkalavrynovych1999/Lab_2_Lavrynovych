n = int(input('Число Петра: '))

saved_numbers = []
is_current = False

while True:

    answer = input('Варіанти Ольги (числа через кому): ')

    if answer == str(n):
        print('Ура!')
        break

    if answer == 'HELP':
        if saved_numbers:
            print('Число є серед ', str(saved_numbers))
            continue
        else:
            print('Ольга ще не називала це число')
            continue
    else:
        nums = answer.split(',')
        for num in nums:
            if int(num) == n:
                saved_numbers = answer
                is_current = True

        if is_current:
            print('YES')
        else:
            print('No')

        is_current = False
