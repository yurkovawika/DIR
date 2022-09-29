import openpyxl
wb = openpyxl.reader.excel.load_workbook(filename = 'dir_phone.xlsx')

def delete_data_xlsx(i):
    ws = wb.active
    ws.delete_rows(i+1)
    wb.save('dir_phone.xlsx')

def delete_data_all_xlsx():
    ws = wb.active
    while ws.max_row > 1:
        ws.delete_rows(2)
    wb.save('dir_phone.xlsx')

# def save():
#     wb.save('dir_phone.xlsx')