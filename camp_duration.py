import calendar
from datetime import datetime


def check_valid_date(camp_begin, camp_end):
    is_valid_date = (
                    ((camp_begin.month == datetime.now().month)
                        and (camp_begin.year == datetime.now().year)
                        and (camp_begin.day - datetime.now().day <= 5))
                    or ((camp_begin.year == camp_end.year)
                        and (camp_end.month < camp_begin.month))
                    or (camp_end.year < camp_begin.year)
                    or (int((camp_end - camp_begin).days) > 365)
                    or (int((camp_begin - datetime.now()).days) > 365)
                    or ((camp_begin.month < datetime.now().month)
                        and (camp_begin.year == datetime.now().year)))
    return is_valid_date


def camp_duration_one_year(camp_begin, camp_end):
    second_to_last_month = camp_begin.month
    duration_first_month = \
        calendar.monthrange(camp_begin.year, camp_begin.month)[1]\
        - camp_begin.day + 1
    camp_days_in_month = [duration_first_month]
    # days_in_month={f'{camp_begin.month}':calendar.monthrange(camp_begin.year,camp_begin.month)[1]}
    duration_in_between = 0
    for months_in_camp in range((camp_end.month-camp_begin.month-1)):
        second_to_last_month += 1
        duration_in_between += \
            calendar.monthrange(camp_end.year, second_to_last_month)[1]
        camp_days_in_month.append(calendar.monthrange(camp_end.year, second_to_last_month)[1])
    duration_last_month = camp_end.day
    camp_days_in_month.append(camp_end.day)
    duration = duration_first_month + duration_last_month + duration_in_between
    return(duration, camp_days_in_month)


def camp_duration_with_year_transition(camp_begin, camp_end):
    duration_first_month =\
        calendar.monthrange(camp_begin.year, camp_begin.month)[1] \
        - camp_begin.day + 1
    camp_days_in_month = [duration_first_month]
    second_to_last_month = camp_begin.month
    duration_in_year_1 = 0
    for months_in_camp in range((12-camp_begin.month)):
        second_to_last_month += 1
        duration_in_year_1 +=\
            calendar.monthrange(camp_begin.year, second_to_last_month)[1]
        camp_days_in_month.append(calendar.monthrange(camp_begin.year, second_to_last_month)[1])
    second_to_last_month = 0
    duration_in_year_2 = 0
    for months_in_camp in range((camp_end.month-1)):
        second_to_last_month += 1
        duration_in_year_2 += \
            calendar.monthrange(camp_end.year, second_to_last_month)[1]
        camp_days_in_month.append(calendar.monthrange(camp_end.year, second_to_last_month)[1])
    duration_last_month = camp_end.day
    camp_days_in_month.append(duration_last_month)
    duration = duration_first_month+duration_last_month+duration_in_year_1 \
        + duration_in_year_2
    return(duration, camp_days_in_month)


def camp_duration_one_month(camp_begin, camp_end):
    duration = (camp_end.day-camp_begin.day) + 1
    camp_days_in_month = [duration]
    return duration, camp_days_in_month


def camp_duration(camp_begin, camp_end):

    camp_begin = datetime.strptime(camp_begin, '%m/%d/%Y')
    camp_end = datetime.strptime(camp_end, '%m/%d/%Y')
    if check_valid_date(camp_begin, camp_end):
        raise ValueError("Пожалуйста, проверьте правильность дат в кампании.")
    elif camp_end.month == camp_begin.month and camp_end.year == camp_begin.year:
        duration_result = camp_duration_one_month(camp_begin, camp_end)
        return duration_result
    elif (camp_end.month-camp_begin.month >= 1) \
        and (camp_end.year == camp_begin.year):
        duration_result = camp_duration_one_year(camp_begin, camp_end)
    elif camp_end.year > camp_begin.year:
        duration_result =\
             camp_duration_with_year_transition(camp_begin, camp_end)
    else:
        raise ValueError("Даты кампании не были введены \
            или указаны в несоответствующем формате")
    return duration_result


if __name__ == "__main__":
    print(camp_duration('12/30/2019', '12/31/2019'))
    print(camp_duration('12/30/2019', '05/31/2020'))
    print(camp_duration('12/30/2019', '01/12/2020'))
    print(camp_duration('02/10/2020', '04/12/2020'))
    print(camp_duration('08/12/2019', '03/12/2020'))
