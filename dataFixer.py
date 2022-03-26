import csv
import pandas as pd

#opening the csv file
file = open('test_data.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)

#taking all csv lines in to an object
rows = []
for row in csvreader:
        rows.append(row)
file.close()


df = pd.DataFrame(row)
print (df)

#formatting the dates--------------------

#starting date
day = 4
month = 10
year = 21

#using a while loop to have more control over testing
i=0
while i<20:
        #print (rows[i][2])
        i+=1

#filename = 'train_data_fixed.csv'
#with open(filename, 'w', newline="") as file:
#    csvwriter = csv.writer(file) # 2. create a csvwriter object
#    csvwriter.writerow(header) # 4. write the header
#    csvwriter.writerows(data) # 5. write the rest of the data
