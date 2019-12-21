import calendar
from datetime import datetime


def check_valid_date(camp_begin, camp_end):
    camp_begin = datetime.strptime(camp_begin,'%m/%d/%Y')
    camp_end = datetime.strptime(camp_end, '%m/%d/%Y')
    is_valid_date = (
                    ((print(datetime.now().month => camp_begin.month) and print(camp_begin.year == datetime.now().year) and print(camp_begin.day - datetime.now().day <= 5)))
                    or ((camp_begin.year == camp_end.year) and (camp_end.month < camp_begin.month))
                    or  (camp_end.year < camp_begin.year)
                    or  ((camp_end.year-camp_begin.year) >= 2))
    return is_valid_date

#print(check_valid_date('12/27/2019', '12/31/2019'))
#print(check_valid_date('12/30/2019', '12/31/2019'))
#print(check_valid_date('12/30/2019', '01/12/2020'))
# print ((datetime.now().month <= camp_begin.month), (camp_begin.year == datetime.now().year), (camp_begin.day - datetime.now().day <= 5))
#print(check_valid_date('02/10/2020', '04/12/2020'))
print(check_valid_date('08/12/2019', '03/12/2020'))
