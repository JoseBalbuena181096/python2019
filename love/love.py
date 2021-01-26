#!/usr/bin/env python3
import time

def heart(s):
    for row in range(6):
        for col in range(7):
            if(row==0 and col%3!=0)or(row==1 and col%3==0) or (row-col==2) or (row+col==8):
                print (s+" ",end="")
            else:
                print(" ",end=" ")
        print("")


emoji = ["\U0001F498","\U0001F970","\U0001F60D","\U0001F929","\U0001F618","\U0001F97A","\U0001F63B","\U0001F648"]
text = ["Te amo","Eres mu especial","No puedo olvidar", "Mi reina","Mi cielo","Mi amor","Me haces muy feliz","Te amo"]
i=0
print("")
for e in emoji:
    print(text[i])
    heart(e)
    print("")
    time.sleep(1)
    i+=1
