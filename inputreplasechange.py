def input_contakt():
    return input('Введитe фамилию, имя, телефон, описание(15 символов) через пробел.\n').title().split()

def search(book):
    temp_book = book['str'] + book['lst']
    flag = True
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя:\n")
    for line in temp_book:
        if ans in line.lower():
            flag = False
            print("-" * len(line))
            print(line)
            print("-" * len(line))
    if flag:
        print()
        print('===>> Такой записи еще нет, если хотите добавить новую, то нажмите 2 или 3! <<===')
        print()

def delete_contact(book):
    flag = True
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя: ")
    for line in book:
        if ans in line:
            flag = False
            old_result = line
            break                 
    if flag:
        print()
        print('===>> Такой записи еще нет, если хотите добавить новую, то нажмите 1 или 2! <<===')
        print()
    return old_result

def replace_contact(book):
    flag = True
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя: ")
    for line in book:
        if ans in line:
            flag = False
            old_result = line
            result = line.split(", ")            
            change = input(
                "Что именно вы хотите изменить? Введите 'Имя', 'Фамилия', 'Номер', 'Комментарий': ")
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
    return result, old_result # Изменил
