#добавление данных в файл
import openpyxl




def add_data_txt(data): #заполнение файла txt
    with open(u'dir3.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')


def add_data_xlsx(z):
    wb = openpyxl.reader.excel.load_workbook(filename='dir_phone.xlsx')
    sheet = wb.active
    y = sheet.max_row + 1
    z = z+y
    for i in range(y, z):
        sheet['A' + str(i)] = input('Введите имя: ')
        sheet['B' + str(i)] = input('Введите фамилию: ')
        sheet['C' + str(i)] = input('Введите номер телефона: ')
        wb.save('dir_phone.xlsx')