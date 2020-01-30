import openpyxl
from collections import Counter
import string
from openpyxl import load_workbook


wb = load_workbook('test.xlsx')
worksheet = wb['APR_Market']
headers = []
for colnum in range(1, worksheet.max_column +1):
    headers.append(worksheet.cell(column=colnum, row=10).value)
print (headers)
data_from_market = []
for row in range(11, worksheet.max_row +1):
    line = {}
    for header in headers:
        cell_value = worksheet.cell(column=headers.index(header)+1,row=row).value
        if type(cell_value) == 'str':
            cell_value = cell_value.strip()
        elif type(cell_value) == 'int':
            cell_value = str(cell_value)
        elif cell_value is None:
            pass
        line[header] = cell_value
        data_from_market.append(line)
print(data_from_market[0:6])
#print(data_from_market)
#print(data_from_market[0])
#billboards_data = {}
#for line in data_from_market:
    #if str(line["Способ показа"]) == "Экран"and line["OTS"] is not None:
     #   if line["GID"][:10] not in billboards_data.keys():
      #      billboards_data.update({f'{line["GID"][:10]}':[ float(line["OTS"]),  float(line["Выходов в сутки"]), str(line['Адрес поверхности'])] })
            
                #billboards_data.update({f'{line["GID"][:10]}':[ float(b),  float(line["Выходов в сутки"]), str(line['Адрес поверхности'])] })
       # else:
        #    billboards_data[f'{line["GID"][:10]}'][1] += float(line["Выходов в сутки"]) 
    #else:
     #   raise ValueError("не хватает данных")
#print(billboards_data) 


#def text_finder(billboards_data):
 #   for key in billboards_data
  #  for bb in billboards_data:
   # if bb[:9] == 'MSBB04620' or bb[:9] == 'MSBB15852':
       # if 'до Х' in bb_adress[bb]:
            
        #elif 'в центр' in in bb_adress[bb]:
        

        

