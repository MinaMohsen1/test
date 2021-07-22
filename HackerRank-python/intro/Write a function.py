def is_leap(year):
    x=year%4==0 and (year%400==0 or year %100 !=0)
    return x

year = int(input())
print(is_leap(year))
