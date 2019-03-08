import csv

with open("personal_data.csv","w",newline="") as personal_data:
    writer=csv.writer(personal_data,delimiter=",")
    writer.writerows([
        ("S/N","Name", "Number", "Email"),
        (1,"Emily Ong", 12345, "e@mail.com"),
        (2,"Emily Ang", 12346, "e1@mail.com"),
        (3,"Emily Lim", 12347, "e2@mail.com"),
        (5,"Emily Ng", 12348, "e3@mail.com"),
        ])
personal_data.close()
with open("personal_data.csv","r",newline="") as file:
    records=csv.reader(file,delimiter=",")
    for record in records:
        print(record[0:4])
personal_data.close()
