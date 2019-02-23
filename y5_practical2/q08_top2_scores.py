#8 (Finding the two highest scores) q08_top2_scores.py
#Write a program that prompts the user to enter the number of
#students and each student's name and score, and finally displays
#the student with the highest score and the student with the
#second-highest score.

num_of_students=int(input("Number of students: "))
names=[]
scores=[]
for i in range(num_of_students):
    name,score=input().split()
    names.append(name)
    scores.append(int(score))

index_a=0
index_b=1
name_a=0
name_b=0
cmp=0
for i in range(num_of_students):
    if scores[i]>cmp:
        cmp=scores[i]
        index_b=index_a
        index_a=i
        name_a=names[index_a]
        name_b=names[index_b]
print("Highest scorer:",name_a)
print("Second-highest scorer:",name_b)
