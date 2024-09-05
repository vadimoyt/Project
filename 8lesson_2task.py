while True:
    try:
        first_number = float(input('Введите первое число'))
        action = input('Выберите действие: +, -, /, *')
        list_of_action = ['+', '-', '/', '*']
        while action not in list_of_action:
            print('Неверное действие, попробуйте еще раз')
            action = input('Выберите действие: +, -, /, *')
        second_number  = float(input('Введите второе число'))
        if action == '+':
            print(first_number + second_number)
        elif action== '-':
            print(first_number - second_number)
        elif action== '/':
            print(first_number / second_number)
        elif action== '*':
            print(first_number * second_number)
        break
    except ValueError:
        print('Это не число, попробуйте заново')

