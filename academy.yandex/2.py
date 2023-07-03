name = input('Как Вас зовут?')
print(f'Здраствуйте, {name}!')
hay = input('Как дела?')
match hay:
    case 'хорошо':
        print('Я за вас рада!')
    case 'плохо':
        print('Всё наладится!')