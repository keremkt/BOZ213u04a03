
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res


def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if md != None and day >= 1 and day <= md:
        return days + day
    else:
        return None


print(day_of_year(2000, 12, 31))

test_dates = [(2000, 12, 31), (2001, 12, 31), (2016, 3, 1), (2023, 2, 29), (2023, 13, 1), (1500, 1, 1)]
test_results = [366, 365, 61, None, None, None]
for i in range(len(test_dates)):
    yr, mo, dy = test_dates[i]
    print(yr, mo, dy, "-> ", end="")
    result = day_of_year(yr, mo, dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
