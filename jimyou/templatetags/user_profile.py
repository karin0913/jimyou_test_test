from django import template
from math import modf
register = template.Library()
import datetime
from datetime import datetime as dt
from datetime import timedelta
from dateutil import parser, relativedelta
import re
 
@register.simple_tag
def user_profile(check):

    print(check)
    return check
       