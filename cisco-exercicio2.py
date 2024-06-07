def is_year_leap(year):
    if y%400==0:
        return True
    if y%100==0:
        return False
    if y%4==0:
        return True
    else:
        return False
        
year = int(input("Enter year to be checked:"))
value = is_leap_year(year)
if value:
    print("Is a leap year.")
else:
    print("Is not a leap year.")

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
