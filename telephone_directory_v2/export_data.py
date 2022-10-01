#Экспорт данных в файл txt
import openpyxl
import sql_data as sd

def export_data_xlsx():
    wb = openpyxl.Workbook()
    wb.save('dir_phone.xlsx')
    wb = openpyxl.reader.excel.load_workbook(filename='dir_phone.xlsx')
    sheet = wb.active
    for i in range(1, sd.f()+1):
        sheet['A' + str(i)] = sd.export_xlsx('fname',i)
        sheet['B' + str(i)] = sd.export_xlsx('lname',i)
        sheet['C' + str(i)] = sd.export_xlsx('t_phone',i)
    wb.save('dir_phone.xlsx')


def export_data_txt():
    with open('dir_phone.txt', 'w', encoding='utf-8') as file:
        for i in range(1,sd.f()+1):
            file.write(f'{sd.export_xlsx("fname",i)};')
            file.write(f'{sd.export_xlsx("lname", i)};')
            file.write(f'{sd.export_xlsx("t_phone", i)};\n')




    
