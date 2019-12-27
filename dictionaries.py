students = {"Bob":12, "Rachel":13, "Emily":15}
print(students["Rachel"])

students["Rachel"] = 15
print(students["Rachel"])

del students["Rachel"]
print(students)
print(len(students))

students = {"Bob":12, "Bob":13, "Bob":15}
print(students["Bob"])
