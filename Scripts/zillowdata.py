import xml.etree.ElementTree as ET
import urllib
import datetime

def get_house_value(address, csz):
	#This method returns a tuple (currValue, soldValue)
	#Format of address = "14232 Shady Oak Ct"
	#Format of csz = "Saratoga, CA"
	if(address == '' or csz == ''):
		return address, csz, 0
	params = urllib.urlencode({'zws-id':'X1-ZWz1bbf8u6dqff_a1050', 'address':address, 'citystatezip':csz})
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

filenames = ['Data/donor_data.csv', 'Data/donor_data2.csv']
user_id = 0

for filename in filenames:
	f = open(filename, 'r')
	output = open('Data/donor_features.csv', 'w')
	donations = f.readlines()[0].split('\r')
	donations.pop(0)
	output.write("id, city, state, donation, house_price, house_sold_at, years_sold\n")
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
		out = "%d, %s, %s, %s, %s, %s, %d\n"%(user_id, city, state, amount, currVal, soldVal, years)
		output.write(out)
		user_id = user_id + 1
	f.close()
output.close()
