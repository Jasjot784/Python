primes=[2,3,5,7]
for num in primes:
    print(num)
print("Outside the for loop")

list1 = ["Apple","Bananas","Cherries"]
tup1 = (13,12,15)
for item in list1:
    print(item)
for item in tup1:
    print(item)

for i in range(1,11):
    print(i)

for i in range(0,11,2):
    print(i)

for i in range(0,5):
    for j in range(0,3):
        print(i*j)
