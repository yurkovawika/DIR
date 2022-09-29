#Создание и сохранение файлов txt или xlsx
import openpyxl

def create_file_xlsx():#создание файла excel
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Имя'
    sheet['B1'] = 'Фамилия'
    sheet['C1'] = 'Номер телефона'
    wb.save('dir_phone.xlsx')
create_file_xlsx()


