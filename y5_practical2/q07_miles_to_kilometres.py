#7 (Conversion from miles to kilometres) q07_miles_to_kilometres.py
#Write a program that displays the following two tables side-by-side
#(note that 1 mile is 1.609 kilometres):

def miles_to_kilo(num_m1,num_m2,num_k1,num_k2):
    print("Miles Kilometres Kilometres Miles")
    for i in range(num_m1-1,num_m2):
        #\t
        size_a=6-len(str(i+1))
        space_a=" "*size_a
        size_b=11-(len(str(int((i+1)*1.609)))+3)-3
        space_b=" "*size_b
        size_c=11-len(str(num_k1))
        space_c=" "*size_c
        print("{0}{2}{1:.3f}".format(i+1,(i+1)*1.609,space_a),
              space_b,
              "{0}{2}{1:.3f}".format(num_k1,(num_k1)*1.609,space_c))
        num_k1+=5

miles_to_kilo(1,10,20,65)
