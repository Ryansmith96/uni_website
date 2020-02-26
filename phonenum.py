#!/usr/bin/env python3.8  
#thenumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def create_phone_number(thenumber):
    pt1 = thenumber[0:3]
    pt2 = thenumber[3:6]
    pt3 = thenumber [6: ]

    sep = ","
    pt1str = "".join(map(str,pt1))
    pt2str = "".join(map(str,pt2))
    pt3str = "".join(map(str,pt3))
    print("(" + pt1str + ")" + " " + pt2str +"-" + pt3str)




create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
   

