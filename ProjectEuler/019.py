# All of these calculations are based on the fact that Jan 1, 1900 is a Monday

def isLeapYear(year):
	if(year == 1900):
		return False
	else:
		return year % 4 == 0

def daysPerYear(year):
	if(isLeapYear(year)):
		return 366
	else:
		return 365


# Create array where value indicates which day marks a new year
newYearDays = []
leapYears = []
totalDays = 0
newYearDays.append(0)
for y in range(1900, 2001):
	totalDays += daysPerYear(y)	# Total number of days from Jan 1 1900 to Dec 31 2000
								# Equals to 36890
	newYearDays.append(totalDays)
	leapYears.append(isLeapYear(y))

normalYearMonthDays = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
leapYearMonthDays = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

def isLeapYearDay(day):
	for e in range(len(newYearDays)):
		if(day<newYearDays[e]):
			return leapYears[e-1]

def isFirstOfMonth(day):
	limit = 0
	for l in range(len(newYearDays)):
		if(day<newYearDays[l]):
			limit = newYearDays[l-1]
			break

	monthDay = day - limit
	isLeap = isLeapYearDay(day)

	if(isLeap):
		dayList = leapYearMonthDays
	else:
		dayList = normalYearMonthDays
	
	for d in dayList:
		if(monthDay == d):
			return True
	
	return False

def isSunday(day):
	weekDay = day % 7
	if(weekDay == 6):	# Mon is 0, Tue is 1, ..., Sun is 6
		return True
	else:
		return False

count = 0
for i in range(365, totalDays): # We are starting on the year 1901, not 1900
	if(isFirstOfMonth(i) and isSunday(i)):
		count += 1

print(count) # 171
