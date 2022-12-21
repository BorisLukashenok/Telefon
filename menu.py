import readandwrite
import scan


file_bok_str = 'Book1.txt'
file_bok_list = 'Book2.txt'

dict_command = {'1':  scan, '2': readandwrite.addcontactstr}
print('''Команды для работы со справочником:
     Выход из программы: 0 или Enter
     Просмотр всех записей обоих справочников:  - 1
     Добавление новой записи в строковый справочник: -2
     Добавление новой записи в списочный справочник:- 3
     Удаление записи из справочника по номеру записи: - 4
     Изменение записи из справочника по номеру записи: - 5 ''')

while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command]()
    else:
        print(' command error!')
