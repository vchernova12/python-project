from camp_duration import camp_duration
from avg_discount import avg_discount
from excel_1 import data_transfer
from lp import lp_constractor
import openpyxl

# Initialize a workbook 


def final(budget, camp_begin, camp_end, discounts):
    duration, camp_days_in_month = camp_duration(camp_begin, camp_end)
    avg_discount_1 = avg_discount(discounts, camp_days_in_month, duration)
    in_stock, billboards_costs, billboards = data_transfer(duration, avg_discount_1)
    result_value = lp_constractor(budget, billboards, in_stock, billboards_costs)
    
    wb = openpyxl.Workbook()

# добавляем новый лист
    wb.create_sheet(title = 'Первый лист', index = 0)

# получаем лист, с которым будем работать
    sheet = wb['Первый лист']


# Loop over the rows and columns and fill in the values
    for row in range(1, len(result_value)):

        #for col in range(1, 2):
        #print([list(result_value.items())[row-1]])
        sheet.append(list(result_value.items[row-1])
    wb.save('example.xlsx') 


if __name__ == "__main__":
    print(final(350000, '03/01/2020', '04/30/2020', [0.3, 0.4])) 