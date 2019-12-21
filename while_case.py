import calendar
from datetime import datetime
camp_begin= input('начало кампании')
camp_end=input('конец кампании')

camp_begin= datetime.strptime(camp_begin, '%m/%d/%Y')
camp_end= datetime.strptime(camp_end, '%m/%d/%Y')
if camp_end.month - camp_begin.month == 1:
    duration_first_month = int(calendar.monthrange(camp_begin.year,camp_begin.month)[1]) - camp_begin.day + 1
    duration_last_month = camp_end.day
    duration_2_months=duration_first_month + duration_last_month
    print(duration_2_months)
elif camp_end.month-camp_begin.month > 1:
    second_to_last_month=camp_begin.month
    print(second_to_last_month)
    duration_in_between=0
    while second_to_last_month < camp_end.month:
        second_to_last_month +=1
        duration_in_between += calendar.monthrange(camp_end.year,second_to_last_month)[1]
        print(duration_in_between, second_to_last_month,camp_end.month)
    duration_first_month = calendar.monthrange(camp_begin.year,camp_begin.month)[1] - camp_begin.day +1 
    duration_last_month = camp_end.day
    duration = duration_first_month+duration_last_month+duration_in_between
    print(duration,duration_in_between)
else:
    duration = (camp_end.day-camp_begin.day)+1
    print(duration) 

