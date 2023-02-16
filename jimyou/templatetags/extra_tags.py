from django import template
from math import modf
register = template.Library()
import datetime
from datetime import datetime as dt
from datetime import timedelta
from dateutil import parser, relativedelta
import re
 
@register.simple_tag
def time_stamping(birthday,gender,country):
        gender = gender
        country = country
        if gender == 'M' and country == 'ja':
            item = '1'
            m0 = 81
            m10 = 5
            m20 = 22
        elif gender == 'F' and country == 'ja':
            item = '2'
            m0 = 87
            m10 = 6
            m20 = 9
        elif gender == 'U' and country == 'ja':
            item = '3'
            m0 = 81
            m10 = 5
            m20 = 22

        if gender == 'M' and country == 'us':
            item = '1'
            m0 = 73
            m10 = 5
            m20 = 27
        elif gender == 'F' and country == 'us':
            item = '2'
            m0 = 79
            m10 = 3
            m20 = 18
        elif gender == 'U' and country == 'us':
            item = '3'
            m0 = 73
            m10 = 5
            m20 = 27

        if gender == 'M' and country == 'uk':
            item = '1'
            m0 = 79
            m10 = 1
            m20 = 1
        elif gender == 'F' and country == 'uk':
            item = '2'
            m0 = 82
            m10 = 10
            m20 = 27
        elif gender == 'U' and country == 'uk':
            item = '3'
            m0 = 79
            m10 = 1
            m20 = 1

        if gender == 'M' and country == 'ch':
            item = '1'
            m0 = 75
            m10 = 1
            m20 = 1
        elif gender == 'F' and country == 'ch':
            item = '2'
            m0 = 80
            m10 = 1
            m20 = 1
        elif gender == 'U' and country == 'ch':
            item = '3'
            m0 = 81
            m10 =1 
            m20 = 1
        print(gender)
        birthday = str(birthday)
        birthday = re.sub(r"\D","",birthday)
        date = birthday
        # date = '20020101'
        date = datetime.datetime.strptime(date, '%Y%m%d')
        date = date + relativedelta.relativedelta(years=m0)
        date = date + relativedelta.relativedelta(months=m10)
        date = date + relativedelta.relativedelta(days=m20)
        now = datetime.datetime.now()
        i = now.strftime('%Y%m%d')
        n = date.strftime('%Y%m%d') 
        m = int(n)-int(i)
        item = date - now
        w = date.year
        o = now.year
        a = date.month
        b = now.month
        c = date.day
        d = now.day
        s = w - o
        q = a - b
        r = c -d
        if r < 1:
            r = r+30
            q = q -1
        if q < 1:
            q = q+12
            s = s -1
        if r > 30:
            r = 1
            q = q +1
        if q > 12:
            q = 1
            s = s +1
        # now = datetime.datetime.now()
        # d = now.strftime('%Y/%m/%d')
        print(type(date))
        print(type(now))
        print(type(item))
        print(type(i))
        print(type(n))
        print(type(m))
        return s