def word_number(i):
	if(i == 1):
		return "one"
	elif(i == 2):
		return "two"
	elif(i == 3):
		return "three"
	elif(i == 4):
		return "four"
	elif(i == 5):
		return "five"
	elif(i == 6):
		return "six"
	elif(i == 7):
		return "seven"
	elif(i == 8):
		return "eight"
	elif(i == 9):
		return "nine"
	elif(i == 10):
		return "ten"
	elif(i == 11):
		return "eleven"
	elif(i == 12):
		return "twelve"
	elif(i == 13):
		return "thirteen"
	elif(i == 14):
		return "fourteen"
	elif(i == 15):
		return "fifteen"
	elif(i == 16):
		return "sixteen"
	elif(i == 17):
		return "seventeen"
	elif(i == 18):
		return "eighteen"
	elif(i == 19):
		return "nineteen"
	elif(i == 20):
		return "twenty"
	elif(i>= 21 and i<=29):
		return word_number(20) + word_number(i%10)
	elif(i == 30):
		return "thirty"
	elif(i>=31 and i<=39):
		return word_number(30) + word_number(i%10)
	elif(i == 40):
		return "forty"
	elif(i>=41 and i<=49):
		return word_number(40) + word_number(i%10)
	elif(i == 50):
		return "fifty"
	elif(i>=51 and i<=59):
		return word_number(50) + word_number(i%10)
	elif(i == 60):
		return "sixty"
	elif(i>=61 and i<=69):
		return word_number(60) + word_number(i%10)
	elif(i == 70):
		return "seventy"
	elif(i>=71 and i<=79):
		return word_number(70) + word_number(i%10)
	elif(i == 80):
		return "eighty"
	elif(i>=81 and i<=89):
		return word_number(80) + word_number(i%10)
	elif(i == 90):
		return "ninety"
	elif(i>=91 and i<=99):
		return word_number(90) + word_number(i%10)
	elif(i>=100 and i<=900 and i%100==0):
		return word_number(int(i/100)) + "hundred"
	elif(i == 1000):
		return "onethousand"
	else:
		return word_number(int(i/100)*100) + "and" + word_number(i%100)

maximum = 1000
string = ""
for i in range(1,maximum+1):
	string += word_number(i)

print(len(string)) #21124
