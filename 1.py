file_bok_list = 'Book1.txt'
file_bok_str = 'Book2.txt'

def readfile_list(file_bok):
    with open(file_bok, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ''), s.readlines()))

def print_book():
    # Просмотр всех записей справочника из двух файлов:
    data1 = readfile_list(file_bok_str)
    data2 = readfile_list(file_bok_list)
    print("-" * 22)
    for i in data1:
        if i != "":
            print(f'|| {i}' + " " * (22 - len(i) - 5) + "||")
        elif i == "":
            print("-" * 22)
            print("-" * 22)
    print("-" * 22 + "\n")
    for i, v in enumerate(data2, 1):
        print(f"{i}) {v}")
        print()

def add_contact_list():
    with open(file_bok_list, "a", encoding="utf_8") as data:
        data.write(", ".join(input().title().split())+"\n")

def add_contact_str():
    with open(file_bok_str, "a", encoding="utf_8") as data:
        data.write(str("\n".join(input().title().split())+'\n\n'))

def search():
    book = readfile_list(file_bok_list)
    flag = True
    ans = input("Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя: ")
    for line in book:
        if ans in line:
            flag = False
            print("-" * len(line))
            print(line)
            print("-" * len(line)) 
    if flag: 
        print()
        print('===>> Такой записи еще нет, если хотите добавить новую, то нажмите 1 или 2! <<===')
        print()

def change_contact():
    book = readfile_list(file_bok_list)
    flag = True
    ans = input("Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя: ")
    for line in book:
        if ans in line:
            flag = False
            result = line.split(", ")
            change = input("Что именно вы хотите изменить? Введите 'Имя', 'Фамилия', 'Номер', 'Комментарий': ")
            name = result[0]
            secondname = result[1]
            number = result[2]
            comment = result[3]
            change_to = input("На что менять?: ")
            if change == "Имя":
                result.remove(name)
                result.insert(0, change_to)
            elif change == "Фамилия":
                result.remove(secondname)
                result.insert(1, change_to)
            elif change == "Номер":
                result.remove(number)
                result.insert(2, change_to)
            elif change == "Комментарий":
                result.remove(comment)
                result.insert(3, change_to)
            else:
                print("Некорректный ввод!!!")
    if flag: 
        print()
        print('===>> Такой записи еще нет, если хотите добавить новую, то нажмите 1 или 2! <<===')
        print()
    return result

# # # словарь команд, в значениях функции их исполняющие
dict_command = {'1':  print_book, '2': add_contact_list, '3': add_contact_str, '4': search, '5': change_contact}

print('''Команды для работы со справочником:
     Просмотр всех записей справочника: - 1
     Добавление новой записи в Book1.txt (В одну строку, запись через пробел) - 2
     Добавление новой записи в Book2.txt (Каждое параметр в разных строках, запись через пробел) - 3
     Поиск необходимого контакта по параметрам - 4
     Выход из программы - 9 ''')

while True:
    command = input('Команда: > ')
    if command in dict_command and command != "9":
        dict_command[command]()
    elif command == "9":
        print()
        print("ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ")
        print()
        break
    elif command not in dict_command:
        print('Команда не распознана, попробуйте снова')




    