def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(f_year, f_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(f_year) == True:
      month_days[1] = 29
      return f"{f_year} is a Leap year, {f_month} month have {month_days[f_month - 1]}"
  else:
      return f"{f_year} is a Leap year, {f_month} month have {month_days[f_month - 1]}"
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(f_year = year, f_month = month)
print(days)




