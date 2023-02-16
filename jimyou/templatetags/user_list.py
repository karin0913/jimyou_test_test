from django import template
from math import modf
register = template.Library()
import datetime
from datetime import datetime as dt
from datetime import timedelta
from dateutil import parser, relativedelta
import re
 
@register.simple_tag
def user_list(gender):
    gender = gender
    if gender == 'M':
        item = '1'
        list = '男性'
    elif gender == 'F':
        item = '2'
        list = '女性'
    elif gender == 'U':
        item = '3'
        list = '未回答'
    print(gender)
    return gender,item,list
       