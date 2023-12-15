from dz_2 import *
CONTACTS =  'Contacts.txt'




def interface():
    while True:
        print('Выбирите действие: \
            \n 1 - Добавить контакт \
            \n 2 - Вывести контакты \
            \n 3 - Найти контакт \
            \n 4 - Копировать контакты по id \
            \n 5 - Кейс 5 \
            \n 0 - Выход ')
        
        
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contacts(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                copy_file(CONTACTS)
            # case 5:
            #     case_5(CONTACTS)


if __name__  == '__main__':
    interface()