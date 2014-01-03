import xml.etree.ElementTree as ET
import urllib
import csv

def get_house_value(address, csz):
	#This method returns a tuple (currValue, soldValue)
	#Format of address = "14232 Shady Oak Ct"
	#Format of csz = "Saratoga, CA"
	if(address == '' or csz == ''):
		return address, csz, ''
	params = urllib.urlencode({'zws-id':'X1-ZWz1bbf8u6dqff_a1050', 'address':address, 'citystatezip':csz})
	url = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?%s"
	zillow_xml = urllib.urlopen(url%params).read()
	root = ET.fromstring(zillow_xml)
	currValue,soldValue,soldDate = '','',''
	for child in root.iter('amount'):
		if(child.text):
			currValue = child.text
	for child in root.iter('lastSoldPrice'):
		if(child.text):
			soldValue = child.text
	for child in root.iter('lastSoldDate'):
		if(child.text):
			soldDate = child.text
	return currValue, soldValue, soldDate

f = open('Data/donor_data.csv', 'r')
output = open('Data/donor_features.csv', 'w')
donations = f.readlines()[0].split('\r')
donations.pop(0)
output.write("Name, Address, City, State, Donation Amount, Current House Price, Price House was Sold At, Date House was Sold, Data Set \n")
for line in donations:
	elements = line.strip().split(',')
	name = elements[1]
	addr = elements[8]
	amount = elements[2]
	csz = elements[10] + ", " + elements[11]
	currVal,soldVal,soldDate = get_house_value(addr, csz)
	out = name + "," + addr + "," + csz + "," + amount + ","
	out += currVal + "," + soldVal + "," + soldDate + ",1" + "\n"
	output.write(out)
f.close()
output.close()