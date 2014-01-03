

out = open('Data/donor_features3.csv', 'w')
in1 = open('Data/donor_features.csv', 'r')
in2 = open('Data/donor_features2.csv', 'r')

for line in in1:
	out.write(line)

#in2.next()
for line in in2:
	out.write(line)

out.close()
in1.close()
in2.close()