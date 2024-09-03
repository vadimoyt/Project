while True:
    try:
        high = float(input('Введите ваш рост в метрах, например: 1.78'))
        weight = float(input('Введите ваш вес в килограмах, например: 78.0'))
        index_wight_body = weight / (high ** 2)
        print('Индекс массы тела равен', format(index_wight_body, '.1f'))
        if 10 < index_wight_body <= 16:
            print('Выраженный дефицит массы тела')
        elif 16 < index_wight_body <= 18.5:
            print('Недостаточная (дефицит) масса тела')
        elif 18.5 < index_wight_body <= 25:
            print('Норма')
        elif 25 < index_wight_body <= 30:
            print('Избыточная масса тела (предожирени')
        if 30 < index_wight_body <= 35:
            print('Ожирение первой степени')
        elif 35 < index_wight_body <= 40:
            print('Ожирение второй степени')
        elif 40 < index_wight_body <= 65:
            print('Ожирение третьей степени (морбидное)')
        elif index_wight_body < 10 or index_wight_body > 65:
            print('Нет данных')
        break
    except ValueError:
        print('Ошибка индексации. Введите параметры заново')
    except ZeroDivisionError:
        print('Некорректные данные, попробуйте заново')
print()
