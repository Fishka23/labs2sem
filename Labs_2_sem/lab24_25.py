znaki_zodiaka = {
    'Овен': ('21 марта', '20 апреля'),
    'Телец': ('21 апреля', '20 мая'),
    'Близнецы': ('21 мая', '21 июня'),
    'Рак': ('22 июня', '22 июля'),
    'Лев': ('23 июля', '23 августа'),
    'Дева': ('24 августа', '22 сентября'),
    'Весы': ('23 сентября', '22 октября'),
    'Скорпион': ('23 октября', '21 ноября'),
    'Стрелец': ('22 ноября', '21 декабря'),
    'Козерог': ('22 декабря', '20 января'),
    'Водолей': ('21 января', '18 февраля'),
    'Рыбы': ('19 февраля', '20 марта')
}

ludi = {
    'Иванов': ('15.04', '25.09'),
    'Петров': ('03.05', '18.11'),
    'Сидоров': ('22.08', '08.03')
}

birthday = input("Введите дату рождения в формате ДД.ММ: ")
day = int(birthday[:2])
month = int(birthday[3:])

if (day >= 21 and month == 3) or (day <= 20 and month == 4):
    sign = 'Овен'
elif (day >= 21 and month == 4) or (day <= 20 and month == 5):
    sign = 'Телец'
elif (day >= 21 and month == 5) or (day <= 21 and month == 6):
    sign = 'Близнецы'
elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
    sign = 'Рак'
elif (day >= 23 and month == 7) or (day <= 23 and month == 8):
    sign = 'Лев'
elif (day >= 24 and month == 8) or (day <= 22 and month == 9):
    sign = 'Дева'
elif (day >= 23 and month == 9) or (day <= 22 and month == 10):
    sign = 'Весы'
elif (day >= 23 and month == 10) or (day <= 21 and month == 11):
    sign = 'Скорпион'
elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
    sign = 'Стрелец'
elif (day >= 22 and month == 12) or (day <= 20 and month == 1):
    sign = 'Козерог'
elif (day >= 21 and month == 1) or (day <= 18 and month == 2):
    sign = 'Водолей'
else:
    sign = 'Рыбы'

print("Люди, родившиеся под знаком зодиака", sign)
for name, birthdate in ludi.items():
    if (birthdate[0] >= znaki_zodiaka[sign][0] and birthdate[0] <= znaki_zodiaka[sign][1]) or \
       (birthdate[1] >= znaki_zodiaka[sign][0] and birthdate[1] <= znaki_zodiaka[sign][1]):
        print(name)