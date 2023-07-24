def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 7):
        if choice == 1: 
            print_result(phone_book) 
        elif choice == 2: 
            name = get_search_name()
            print_result(find_by_name(phone_book, name)) 
        elif choice == 3: 
            number = get_search_number() 
            print_result(find_by_number(phone_book, number))
        elif choice == 4: 
            user_data = get_new_user() 
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5: 
            name = get_search_name() 
            print_result(find_by_name(phone_book, name)) 
            delete_user(phone_book, find_by_name(phone_book, name))
            write_csv('phonebook.csv', phone_book)
        elif choice == 6:  
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Должность"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_txt(filename: str, data: list):
    txt_filename = filename + '.txt'
    print(txt_filename)
    with open(txt_filename, 'w', encoding='utf-8') as fout:
        s = '│'
        fout.write('┌' + '─'*15 + '┬' + '─'*15  + '┬' + '─'*15 + '┬' + '─'*15 + '┐'+'\n')
        fields = ["Фамилия", "Имя", "Телефон", "Должность"]
        for v in fields:
            s += v.center(15) + "│"
        fout.write(f'{s}\n')
        fout.write('├' + '─'*15 + '┼' + '─'*15  + '┼' + '─'*15 + '┼' + '─'*15 + '┤'+ '\n')    

        for i in range(len(data)):
            s = '│'
            for v in data[i].values():
                s += v.center(15) + "│"
            fout.write(f'{s}\n')
            fout.write('├' + '─'*15 + '┼' + '─'*15  + '┼' + '─'*15 + '┼' + '─'*15 + '┤' + '\n')
        fout.write(f'Всего сохранено {len(data)} записей')

def print_result(data: list):
    s = '│'
    print('┌' + '─'*15 + '┬' + '─'*15  + '┬' + '─'*15 + '┬' + '─'*15 + '┐')
    fields = ["Фамилия", "Имя", "Телефон", "Должность"]
    for v in fields:
        s += v.center(15) + "│"
    print(f'{s}')
    print('├' + '─'*15 + '┼' + '─'*15  + '┼' + '─'*15 + '┼' + '─'*15 + '┤')

    for i in range(len(data)):
            s = '│'
            for v in data[i].values():
                s += v.center(15) + "│"
            print(f'{s}')
            print('├' + '─'*15 + '┼' + '─'*15  + '┼' + '─'*15 + '┼' + '─'*15 + '┤')
    print(f'Всего найдено {len(data)} записей')

def find_by_name(data: list, first_name):
    search_by_name = []
    for line in data:
        index = line['Фамилия'].lower()
        if index.find(first_name.lower()) == 0:
            search_by_name.append(dict(line))
    return search_by_name

def find_by_number(data: list, number):
    search_by_number = []
    for line in data:
        index = line['Телефон']
        if  index.find(number) == 0:
            search_by_number.append(dict(line))
    return search_by_number

def get_new_user():
    line = {}
    fields = ["Фамилия", "Имя", "Телефон", "Должность"]
    for v in fields:
        data = input(f'Введите {v}: ')
        line[v] = data
    return line

def delete_user(data: list, name):
    tmp = []
    for record in name:      
        if record in data:
            print('Найдена запись для удаления:')
            tmp.append(record)
            print_result(tmp)
            return
            tmp.clear()
        

def add_user(data: list, user_data: dict):
    data.append(dict(user_data))
    return data

def get_search_name():
    first_name = input("Введите фамилию: ")
    return first_name

def get_search_number():
    name = input("Введите номер: ")
    return name

def get_file_name():
    name = input("Введите имя файла: ")
    return name

work_with_phonebook()
