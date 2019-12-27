read_five_times="No"
count=0
while read_five_times=="No":
    print("Reading Workshop")
    count = count +1
    if(count==5):
      read_five_times="Yes"

print("Good Job!You understood")

c=0
while c<5:
    print(c)
    c=c+1

c=0
while c<5:
    print(c)
    if c==3:
        break
    c=c+1

c=0
while c<5:
    c= c+1
    if c==3:
        continue
    print(c)

c=0
while c<5:
    c= c+1
    if c==3:
        pass
    print(c)
