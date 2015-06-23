import csv

with  open("names.csv","r")as f:
    header = f.readline().split(",")
    atendees1 = []
    csv_f = csv.reader(f)
    for row in csv_f:

        dicti = {}
        for i,j in enumerate(row):

            dicti[header[i].strip()] = j.strip()

        atendees1.append(dicti)



    print atendees1
