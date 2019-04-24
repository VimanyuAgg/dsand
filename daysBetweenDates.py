def nextDay(year, month, day, daysInMonth):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth[month]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def isLeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    if year % 100 != 0 and year % 4 == 0:
        return True
    return False


def validDate(year, month, day, daysInMonth):
    if year <= 0 or month <= 0 or day <= 0:
        return False

    if day > daysInMonth[month]:
        return False

    return True


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. """

    if (year1, month1, day1) == (year2, month2, day2):
        return 0

    daysInMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if isLeapYear(year1):
        daysInMonth[2] = 29

    # program defensively! An assertion to check if the input is not valid!
    assert (validDate(year1, month1, day1, daysInMonth))
    assert (validDate(year2, month2, day2, daysInMonth))
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        if isLeapYear(year1):
            daysInMonth[2] = 29
        else:
            daysInMonth[2] = 28

        year1, month1, day1 = nextDay(year1, month1, day1, daysInMonth)
        days += 1
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()


# def nextDay(year, month, day, hasThirtyOneDays, isLeapYearBool):
#     if month == 2:
#         if isLeapYearBool and day == 28:
#             day += 1
#         elif isLeapYearBool and day == 29:
#             month += 1
#             day = 1
#         elif (not isLeapYearBool) and day == 28:
#             day = 1
#             month += 1
#         else:
#             day += 1
#
#     elif hasThirtyOneDays:
#         if day == 31:
#             month += 1
#             day = 1
#         else:
#             day += 1
#     else:
#         if day == 30:
#             month += 1
#             day = 1
#         else:
#             day += 1
#
#     if month > 12:
#         month = 1
#         year += 1
#
#     return year, month, day
#
#
# def isDate1LessThanDate2(year1, month1, day1, year2, month2, day2):
#     if year1 < year2:
#         return True
#
#     if year1 == year2:
#         if month1 < month2:
#             return True
#
#         elif month1 == month2 and day1 < day2:
#             return True
#
#     return False
#
#
# def validDate(year, month, day, daysInMonth):
#     if year <= 0 or month <= 0 or day <= 0:
#         return False
#
#     if day > daysInMonth[month]:
#         return False
#
#     return True
#
#
# def isLeapYear(year):
#     if year % 100 == 0 and year % 400 == 0:
#         return True
#     if year % 100 != 0 and year % 4 == 0:
#         return True
#     return False
#
#
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """
#     Calculates the number of days between two dates.
#     """
#
#     if (year1, month1, day1) == (year2, month2, day2):
#         return 0
#
#     daysInMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#
#     if isLeapYear(year1):
#         daysInMonth[2] = 29
#
#     assert (validDate(year1, month1, day1, daysInMonth))
#     assert (validDate(year2, month2, day2, daysInMonth))
#
#     assert (not isDate1LessThanDate2(year2, month2, day2, year1, month1, day1))
#
#     days = 0
#     while isDate1LessThanDate2(year1, month1, day1, year2, month2, day2):
#         days += 1
#         isLeapYearBool = False
#         if isLeapYear(year1):
#             isLeapYearBool = True
#         hasThirtyOneDays = True if daysInMonth[month1] == 31 else False
#         year1, month1, day1 = nextDay(year1, month1, day1, hasThirtyOneDays, isLeapYearBool)
#
#     return days
#
#
# def testDaysBetweenDates():
#     # test same day
#     assert (daysBetweenDates(2017, 12, 30,
#                              2017, 12, 30) == 0)
#     # test adjacent days
#     assert (daysBetweenDates(2017, 12, 30,
#                              2017, 12, 31) == 1)
#     # test new year
#     #     print(daysBetweenDates(2017, 12, 30, 2018, 1,  1))
#
#     assert (daysBetweenDates(2017, 12, 30,
#                              2018, 1, 1) == 2)
#     #     # test full year difference
#     assert (daysBetweenDates(2012, 6, 29,
#                              2013, 6, 29) == 365)
#
#     print("Congratulations! Your daysBetweenDates")
#     print("function is working correctly!")
#
#
# testDaysBetweenDates()