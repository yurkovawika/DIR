#Управление
import export_data as ed
import sql_data as sd

def menu():
    print('\n')
    print("Операция выполнена")
    x = int(input('Вернуться в главное меню - введите <1>\n выйти - <2>\n -->> '))
    if x == 1:
        team_selection()
    elif x == 2:
        sd.con.close()
        exit()

def team_selection():
    num = int(input('Какую операцию вам необходимо выполнить:\n'
                    '-Введите <1> чтобы показать данные в консоли\n'
                    '-Введите <2> чтобы добавить данные в справочник\n'
                    '-Введите <3> чтобы удалить данные\n'
                    '-Введите <4> чтобы выполнить экспорт данных в другой файл\n'
                    '-Введите <5> чтобы выйти\n--> '))

    if num ==1:
        print(f"{'-'*10}ВЫВОД ДАННЫХ{'-'*10}")
        print('Какие данные выводим?\n'
                '<1> вывести весь справочник\n'
                '<2> поиск по имени\n'
                '<3> по фамилии\n'
                '<4> по номеру\n')
        num = int(input('--->> '))
        if num == 1:
            print('Показан весь справочник')
            sd.print_db(num)
        elif num == 2:
            sd.print_db(num)
        elif num == 3:
            sd.print_db(num)
        elif num == 4:
            sd.print_db(num)
        menu()

    elif num == 2:
        print(f"{'-'*10}ДОБАВЛЕНИЕ ДАННЫХ В СПРАВОЧНИК{'-'*10}")
        z = 'Y'
        while z in 'Y':
            sd.add_data()
            z = (input('Добавить ещё запись?(Y/N): '))
        menu()

    elif num == 3:
        print(f"{'-'*10}УДАЛЕНИЕ ДАННЫХ ИЗ СПРАВОЧНИКА{'-'*10}")
        print('Что удаляем?\n'
              '<1> Полная очистка\n'
              '<2> Частичное удаление\n')
        num = int(input('--->> '))
        if num == 1:
            print('Полная очистка')
            sd.delete_data(num)
        elif num == 2:
            sd.print_db(1)
            print('\nВведите индекс:')
            z = int(input())
            sd.delete_data(num,z)
        menu()

    elif num == 4:
        print(f"{'-'*10}ЭКСПОРТ ДАННЫХ{'-'*10}")
        print('В какой формат экспортируем?\n'
              '<1> xlsx\n'
              '<2> txt\n')
        num = int(input('--->> '))
        if num == 1:
            print("Экспорт выполнен в файл dir_phone.xlsx")
            exit(ed.export_data_xlsx())
        elif num == 2:
            print("Экспорт выполнен в файл dir_phone.txt")
            exit(ed.export_data_txt())
        menu()
    else:
        exit()

