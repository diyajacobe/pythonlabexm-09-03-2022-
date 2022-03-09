import csv
with open("f.csv",newline="")as csvfile:
    d=csv.DictReader(csvfile)
    print("Number Name Mark Subject")
    print("-----------------")
    for i in d:
        print(i['Number'],i['Name'],i['Mark'],i['Subject'])