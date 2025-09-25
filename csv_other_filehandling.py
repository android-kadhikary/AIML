import csv
file = open("details.csv","r") 
reader = csv.reader(file)
# for row in reader:
#     print(row)  

# with open("details2.csv", "w", newline="") as file1:
#     writer_csv= csv.writer(file1)
#     writer_csv.writerow(["age", " name", " loc",])
#     writer_csv.writerow([30, " aa", " OK"])
#     writer_csv.writerow([25, " bb", " NY"])



with open("details2.csv", "r") as file2:  # append mode
    file2_readmode = csv.reader(file2)
    for r in file2_readmode:
        print(r)    


with open("details2.csv", "r") as file2:  # append mode
    file2_readmode = csv.DictReader(file2)
    for r in file2_readmode:
        print(r)         