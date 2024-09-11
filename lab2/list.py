List=["geeks", "for", "geeks"]
print("\nList Items:")
print(List[0])
print(List[1])
print(List[2])

List2=[10,22,223,820]
print(len(List2))

[["Geeks,for"],["geeks"]] # multi-dimensional list

List2.append(1)
List2.append(44)
print(List2)

# adding elements to the list using iterator
for i in range(1,4):
    List2.append(i)
    print(List2)

#   addition of list to a list
    List.append(List2)
    print("\nList after addition of a list:")
    print(List)

    List3=["hello","ladies"]
    List3.insert(0,9976)
    print(List3)