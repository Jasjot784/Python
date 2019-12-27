countries = ['India','USA','Australia','South Africa']
for country in countries:
    print(country)

shortList = ["a","o","b","c"]
print(shortList[0:2])

shortList.append("b")
print(shortList)

shortList[0] = "c"
print(shortList)

del shortList[1]
print(shortList)

len(shortList)

shortList2 = ["b","j","pb"]
print(shortList+shortList2)
print(shortList*2)

listNum = [1,4,7,23,6]
print(max(listNum))
print(min(listNum))
