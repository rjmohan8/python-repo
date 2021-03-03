flag = 0
character = "#"
count = 4

while flag<=4 and count>=0:
    while flag<=5:
        print(character*flag)
        flag +=1
    while count>=0:
        print(character*count)
        count -=1