import csv,sqlite3
connection=sqlite3.connect("subjects.sqlite")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS subjects_combinations (name TEXT, class TEXT, h1 TEXT, h2a TEXT, h2b TEXT, h2c TEXT);")
with open("exercise1_data.csv","r") as subj_combi:
    records=csv.reader(subj_combi,delimiter=",")
    counter=0
    for record in records:
        if counter>=1:
            cursor.execute("INSERT INTO subjects_combinations (name, class, h1, h2a, h2b, h2c) VALUES (?,?,?,?,?,?)",(record[0],record[1],record[2],record[3],record[4],record[5]))
        counter+=1
cursor.execute("SELECT * FROM subjects_combinations")
results=cursor.fetchall()
username=raw_input()
found=False
username=username.upper()
for result in results:
    if result[0]==username:
        found=True
        print("Good morning "+result[1]+" "+username)
        print("Your subjects: ")
        print("H1"+result[2])
        for i in range(3,6):
            print("H2"+result[i])
if not found:
    print("Your user record is not found in the database")
connection.commit()
connection.close()
