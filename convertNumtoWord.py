units = ['','one','two','three','four','five','six','seven','eight','nine','ten',
	'eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

hundred = ['hundred','thousand','lakh','crore']

def makeHundredUnits(num):
	stri = ''
	if num%100<20:
		stri += units[num%100]
	else:
		stri += tens[num//10]+' '+units[num%10]
	num //= 100
	if num:
		stri = units[num]+' '+hundred[0]+' '+stri
	return stri

def convertNum2Word(num):
	string = makeHundredUnits(num%1000)

	num //= 1000
	i = 1
	while num:
		string = makeHundredUnits(num%100)+' '+hundred[i]+' '+string
		i += 1
		num //=100
	return string

print makeHundredUnits(115)
print convertNum2Word(128512215)
