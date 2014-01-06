import xml.etree.ElementTree as ET
import urllib
import datetime

states = {
	"AL" : 2 ,
	"AK" : 3 ,
	"AZ" : 4 ,
	"AR" : 5 ,
	"CA" : 6 ,
	"CO" : 7 ,
	"CT" : 8 ,
	"DE" : 9 ,
	"DC" : 10 ,
	"FL" : 11 ,
	"GA" : 12 ,
	"HI" : 13 ,
	"ID" : 14 ,
	"IL" : 15 ,
	"IN" : 16 ,
	"IA" : 17 ,
	"KS" : 18 ,
	"KY" : 19 ,
	"LA" : 20 ,
	"ME" : 21 ,
	"MT" : 22 ,
	"NE" : 23 ,
	"NV" : 24 ,
	"NH" : 25 ,
	"NJ" : 26 ,
	"NM" : 27 ,
	"NY" : 28 ,
	"NC" : 29 ,
	"ND" : 30 ,
	"OH" : 31 ,
	"OK" : 32 ,
	"OR" : 33 ,
	"MD" : 34 ,
	"MA" : 35 ,
	"MI" : 36 ,
	"MN" : 37 ,
	"MS" : 38 ,
	"MO" : 39 ,
	"PA" : 40 ,
	"RI" : 41 ,
	"SC" : 42 ,
	"SD" : 43 ,
	"TN" : 44 ,
	"TX" : 45 ,
	"UT" : 46 ,
	"VT" : 47 ,
	"VA" : 48 ,
	"WA" : 49 ,
	"WV" : 50 ,
	"WI" : 51 ,
	"WY" : 52 ,
	}

token = "X1-ZWz1dp4nf26mff_10irx"
def get_house_value(address, csz):
	#This method returns a tuple (currValue, soldValue, years)
	#Format of address = "14232 Shady Oak Ct"
	#Format of csz = "Saratoga, CA"
	if(address == '' or csz == ''):
		return address, csz, 0
	params = urllib.urlencode({'zws-id':token, 'address':address, 'citystatezip':csz})
	url = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?%s"
	zillow_xml = urllib.urlopen(url%params).read()
	root = ET.fromstring(zillow_xml)
	currValue,soldValue,soldDate = '','',''
	years = 0
	for child in root.iter('amount'):
		if(child.text):
			currValue = child.text
	for child in root.iter('lastSoldPrice'):
		if(child.text):
			soldValue = child.text
	for child in root.iter('lastSoldDate'):
		if(child.text):
			soldDate = child.text
	if soldValue and not currValue:
		currValue = soldValue
	elif currValue and not soldValue:
		soldValue = currValue
	if soldDate:
		timeSincePurchase = datetime.datetime.today() - datetime.datetime.strptime(soldDate, '%m/%d/%Y')
		years = timeSincePurchase.days/365
	return currValue, soldValue, years

def get_median_household_income(state, city):
	params = urllib.urlencode({'zws-id':token, 'state':state, 'city':city})
	url = "http://www.zillow.com/webservice/GetDemographics.htm?%s"
	zillow_xml = urllib.urlopen(url%params).read()
	root = ET.fromstring(zillow_xml)
	for child in root.iter('attribute'):
		if(child[0].text and child[0].text== "Median Household Income"):
			return child[1][0][0].text
	return ''

filenames = ['Data/cleaned_data.csv', 'Data/cleaned_data2.csv','Data/akshayapatra_data.csv']
user_id = 0
file_id = 0
output = open('Data/donor_features.csv', 'w')
output.write("id, city, state, donation, house_price, house_sold_at, years_sold, avg_city_income, file_id\n")
for filename in filenames:
	f = open(filename, 'r')
	donations = f.readlines()
	donations.pop(0)
	for line in donations:
		elements = line.strip().split(',')
		name = elements[1]
		addr = elements[8]
		amount = elements[2]
		city = elements[10]
		state = elements[11]
		csz = "%s,%s"%(city, state)
		if not addr or not city or not state:
			continue
		currVal,soldVal,years = get_house_value(addr, csz)
		median_income = get_median_household_income(state, city)
		out = "%d, %s, %d, %s, %s, %s, %d, %s, %d\n"%(user_id, city, states.get(state, 0), amount, currVal, soldVal, years, median_income,file_id)
		output.write(out)
		user_id = user_id + 1
	file_id+=1
	f.close()
output.close()
