from django import template
from math import modf
register = template.Library()
 
@register.filter(name="change_Range")
def change_Range(date_range):
    # 経過年を算出
    fst = date_range/365
    # 整数と少数に分ける decimal=少数
    decimal, year = modf(fst)
 
    # 経過年を差し引いた経過月を算出
    scd = (decimal*365)/(365/12)
    decimal, month = modf(scd)
 
    val = str(round(year))+' 年 '+str(round(month))+' か月'
    return val