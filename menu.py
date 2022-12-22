from function import init_dict, print_book, write_new_contact_list, write_new_contact_str, replace_contact_list, replace_contact_str, delete_contact_str, delete_contact_list
from inputreplasechange import search


def print_hint():
    print('''\nКоманды для работы со справочником:
         Выход из программы: 0 или Enter
         Просмотр всех записей обоих справочников:  - 1
         Добавление новой записи в строковый справочник: -2
         Добавление новой записи в списочный справочник:- 3
         Поиск необходимого контакта по параметрам - 4
         Изменение записи из строкового справочника по данным: - 5
         Изменение записи из списочного справочника по данным: - 6
         Удаление записи из строкового справочника по данным: - 7
         Удаление записи из строкового справочника по данным: - 8 ''')


def menu():

    book_all = init_dict()
    dict_command = {'1': print_book, '2': write_new_contact_str,
                    '3': write_new_contact_list, '4': search, '5': replace_contact_str,
                    '6': replace_contact_list, '7': delete_contact_str, '8': delete_contact_list}
    print_hint()
    while True:
        command = input('Команда: > ')
        if command in dict_command:
            dict_command[command](book_all)
            print_hint()
        elif command == "0" or command == '':
            print()
            print("ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ")
            print()
            break
        else:
            print('Команда не распознана, попробуйте снова')
