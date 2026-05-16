import csv

data=[["name","country","city","skills"],
["Asabeneh","Finland","Helsinki","JavaScript"]]

with open('temp.csv','w',newline='') as file:
   writer= csv.writer(file)
   writer.writerows(data)