#7 (Converting milliseconds to hours, minutes, and seconds)
#Write a method convert_ms(n) that converts milliseconds
#to hours, minutes, and seconds. The method returns a string
#as hours:minutes:seconds. For example, convert_ms(5500)
#returns a string 0:0:5, convert_ms(100000) returns a string
#0:1:40, and convert_ms(555550000) returns a string 154:19:10.

def convert_ms(n):
    #needs more testing
    #1ms=0.001s
    seconds=int(n/1000)
    if seconds<60:
        print("0:0:"+str(seconds))
        return
    elif seconds==60:
        print("0:1:0")
        return
    else:
        minutes=int(seconds%60)
        if (seconds/60)<60:
            print("0:"+str(int(seconds/60))+":"+str(minutes))
        elif (seconds/60)==60:
            print("1:0:"+str(minutes))
        else:
            hours=seconds/60
            print(str(int(hours/60))+":"+str(int(hours-(int(hours/60)*60)))+":"+str(minutes))
    

convert_ms(555550000)
