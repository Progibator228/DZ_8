def data_name_copy_file():
    print('Как назвать файл в который копируем ? ( файл будет с раширением .txt )')
    file_name = input()
    return file_name


def copy_file(file_name):
    with open(file_name, 'r' , encoding='UTF-8') as file:
        all_contact = file.readlines()
        print('Данные с каким id хотим скопировать ?')
        data = int(input())
        data_name = data_name_copy_file()
        copy_data = all_contact[data]
    with open(F'{data_name}.txt', 'w' , encoding='UTF-8') as file:
         file.writelines(copy_data)   


def print_contacts(file_name):
    with open(file_name, 'r' , encoding='UTF-8') as file:
        all_contact = file.readlines()
        if len(all_contact) != 0 :
            for line in all_contact:
                print(line.strip(),'Его уникальный ID =' , all_contact.index(line), end= '\n\n')
        else:
            print('Список пуст')
            


def connect_with_user():
    print('Введите имя и фамилию и телфон (Через пробел)')
    cont_info = input()
    return cont_info

def add_contacts(file_name):
    with open(file_name, 'r' , encoding='UTF-8') as file:
        all_contact = file.readlines()
    nwe_cont = connect_with_user()
    all_contact.append( '\n' +nwe_cont)
    with open(file_name, 'w' , encoding='UTF-8') as file:
        file.writelines(all_contact )
        

def find_contact(file_name):
    with open(file_name, 'r' , encoding='UTF-8') as file:
        all_cont = file.readlines()

    print('Выберите критерий поиска:\
        \n 1 - Имя \
        \n 2 - Фамилия\
        \n 3 - Телефон')
    comm = int(input())
    print('Введите строку для поиска ')
    data = input()
    print('Найденные контакты')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list[comm - 1] == data:
            print(*cont_as_list, 'Его уникальный ID =' , all_cont.index(cont))