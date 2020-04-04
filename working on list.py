list1=["mary","john","laura","peter","peter","paul","jude","luise","kingsley"]
list2=[1,2,3,4,5,6,7,8,9,10]
list1.extend(list2)
list1.append("bertrand")
list1.remove("paul")
list1.insert(6,"felisity")
print(list1)
print(list1.index("jude"))
print(list1.count("peter"))
list2.reverse()
print(list2)

if "laura"  in list1:
    print("true")
else:
    print("no")