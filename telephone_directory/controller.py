#Управление
import add_data
import export_data
import print_data_xlsx
import delete_data
def menu():
    print('\n')
    print("Операция выполнена")
    x = int(input('Вернуться в главное меню - введите <1>\n выйти - <2>\n -->> '))
    if x == 1:
        team_selection()
    elif x == 2:
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
            print_data_xlsx.print_data_all()
        elif num == 2:
            print_data_xlsx.print_data_name()
        elif num == 3:
            print_data_xlsx.print_data_last_name()
        elif num == 4:
            print_data_xlsx.print_data_t_phone()
        menu()

    elif num == 2:
        print(f"{'-'*10}ДОБАВЛЕНИЕ ДАННЫХ В СПРАВОЧНИК{'-'*10}")
        z = int(input('Сколько человек нужно добавить?: '))
        add_data.add_data_xlsx(z)
        print(f"Добавили {z} строк в справочник")
        menu()


    elif num == 3:
        print(f"{'-'*10}УДАЛЕНИЕ ДАННЫХ ИЗ СПРАВОЧНИКА{'-'*10}")
        print('Что удаляем?\n'
              '<1> Полная очистка\n'
              '<2> Частичное удаление\n')
        num = int(input('--->> '))
        if num == 1:
            print('Полная очистка')
            delete_data.delete_data_all_xlsx()

        elif num == 2:
            print_data_xlsx.print_data_all()
            print('\nВведите индекс:')
            i = int(input())
            delete_data.delete_data_xlsx(i)
        menu()

    elif num == 4:
        print(f"{'-'*10}ЭКСПОРТ ДАННЫХ{'-'*10}")
        print('Что экспортируем?\n'
              '<1> Все данные\n'
              '<2> Часть данных по индексу\n')
        num = int(input('--->> '))
        if num == 1:
            export_data.export_data()
        elif num ==2:
            print_data_xlsx.print_data_all()
            print('\nВведите индекс:')
            i = int(input())
            export_data.export_data_id(i)
        menu()
    else:
        exit()

team_selection()