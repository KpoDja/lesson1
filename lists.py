lists = [3, 5, 7, 9, 10.5]
print(lists)

lists.append("Python")
count = len(lists)

print(count)
print(lists[0])
print(lists[-1])
print(lists[2:5])

lists.remove("Python")
print(lists)