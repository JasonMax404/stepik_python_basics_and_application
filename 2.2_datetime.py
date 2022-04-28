# В первой строке дано три числа, соответствующие некоторой дате
# date - год, месяц и день. Во второй строке дано одно число
# days - число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит,
# когда с момента исходной даты date пройдет число дней, равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и
# класс datetime.timedelta﻿ для прибавления дней к дате.

import datetime

(y, m, d) = [int(n) for n in input().split()]
dd = int(input())

date = datetime.date(y, m, d)
delta = datetime.timedelta(days = dd)
new_date = (date + delta).strftime("%Y %#m %#d") #Для Linux: "%Y %-m %-d"
print(new_date)
