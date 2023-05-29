def menu():
    print(
        '1 - Отобразить все контакты \n'
        '2 - Добавить контакт \n'
        '3 - Найти контакт \n'
        '4 - Изменить контакт \n'
        '5 - Удалить контакт \n'
        "6 - Выход \n"
    )
def error():
    return None

def show_contacts(date):
    path = 'file.txt'
    data = open(path, 'r')
    print(data.readlines())
    data.close()



def success(res):
    print ("Сохранено ")

def fail(res):
    print ("Ошибка ")

    

if __name__ == '__main__':
    menu()


