s=str(input())
a=int(input())
hands={'J':10,'Q':10,'K':10,'A':11,'T':10}
ptr=0
res=""
for i in range(a):
    val=0
    card_counter=0
    outcome=False
    while not outcome:
        curr_card=s[ptr]
        card_counter+=1
        if curr_card in hands:
            val+=hands[curr_card]
        else:
            val+=int(curr_card)
        if val>=17 or (card_counter==5 and val<=21):
            if card_counter==2 and val==21:
                res="A"
            elif card_counter==5 and val<=21:
                res="B"
            elif val>21:
                res="D"
            else:
                res="C"+str(val)
            outcome=True
        ptr+=1
print(res)
