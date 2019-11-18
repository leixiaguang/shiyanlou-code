a=0
for a in range(1,101):
    if (a%10 ==7 or a%7 ==0 or a//10 ==7):
        continue
    else:
        print(a)
    a+=1

