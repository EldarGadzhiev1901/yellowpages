import view , model 

def start():
    while True:
        view.welcome()
        view.menu()
        answer = input('Выберете команду, набрав соответствующую цифру ')
        if answer == '1':
            date = model.get_data()
            view.show_contacts(date)
        elif answer == '2':
            contact = input('Задайте данные контакта, через пробел (Имя, фамилия, номер телефона, эл. почта): ')
            res = model.add_contact(contact)
            view.success(res)

        elif answer == '3':
            contact = input('Введите параметры поиска: ')
            result = model.search(contact)

        elif answer == '4':
            contact = input("Введите имя контакта ")
            new = input("Введите новое имя контакта ")
            result = model.change(contact, new )

        elif answer == "5":
            contact = input("Введите имя контакта")
            result = model.delete(contact)
        elif answer == "6":
            break
        else:
            view.error()