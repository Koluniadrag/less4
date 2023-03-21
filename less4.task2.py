phone_num = input("Введіть телефон: ")
if phone_num.isdigit() and len(phone_num) == 10:
    print('Молодець')
else:
    print('Неправильний номер')