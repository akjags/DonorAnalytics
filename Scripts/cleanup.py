

filename = "Data/donor_data2.csv"
f = open(filename, 'r')
output = "Data/cleaned_data2.csv"
out = open(output, "w")
donations = f.readlines()[0].split('\r')
donations.pop(0)

for line in donations:
    out.write("%s\n"%line.strip())


