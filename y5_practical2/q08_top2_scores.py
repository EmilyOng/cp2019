#8 (Finding the two highest scores) q08_top2_scores.py
#Write a program that prompts the user to enter the number of
#students and each student's name and score, and finally displays
#the student with the highest score and the student with the
#second-highest score.

def manual():
    num_of_students=int(input("Number of students: "))
    names=[]
    scores=[]
    curr_max=0
    next_max=0
    index_a=0
    index_b=0
    for i in range(num_of_students):
        name,score=input("Name Score: ").split()
        names.append(name)
        scores.append(int(score))
    for i in range(num_of_students):
        if scores[i]>curr_max:
            index_b=index_a
            index_a=i
            next_max=curr_max
            curr_max=scores[i]
        elif scores[i]>next_max:
            index_b=i
            next_max=scores[i]
    print(names[index_a]+":",curr_max)
    print(names[index_b]+":",next_max)

def auto():
    _num_of_students=int(input("Number of students: "))
    name_score=[]
    for i in range(_num_of_students):
        name,score=input("Name Score: ").split()
        name_score.append((score,name))
    name_score.sort(reverse=True)
    print(name_score[0][1]+":",name_score[0][0])
    print(name_score[1][1]+":",name_score[1][0])

manual()
auto()

#Number of students: 3
#Name Score: fiuhe 24
#Name Score: euheuiv 249
#Name Score: euihveiv 23

#euheuiv: 249
#fiuhe: 24
