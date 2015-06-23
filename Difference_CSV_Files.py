import csv

f = open("names.csv","r")

csv_f = csv.reader(f)
atendent1 = []

for row in csv_f:

	atendent1.append(row[1])
	

print atendent1   
        

    
f.close()

f = open("names2.csv","r")

csv_f = csv.reader(f)
atendent2 = []

for row in csv_f:

	atendent2.append(row[1])
	

print atendent2        
        

    
f.close()


atendent1 = set(atendent1)
atendent2 = set(atendent2)
print atendent2.difference(atendent1)
