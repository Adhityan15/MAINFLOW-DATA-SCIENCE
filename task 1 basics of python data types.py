#TASK 1
#understanding basics of python data types :

#LIST

#creating a list
a=[1,2,3,4,5,6,8]
print("created list ",a)

#acessing the list item of 3 and 4
print("acessed elements of list",a[3:5])

#add items in a list to end 
a.append(11)
print("element added to the list is ",a)

#insert an item as a second position
a.insert(1,12)
print("elements inserted",a)

#remove list items
a.remove(12)
print("element removed from the list",a)

#specified with index
a.pop(3)
print("element specfied",a)
print("-------------------------------------------------------------------------------------------------------------------")

#TUPLE

#creating a tuple
b=(1,2,3,11,5,6,7,9)
print("created tuple",b)

#concatenation (adding)
c=(2,3,4,6)
print("after concatenation",b+c)

#deletion
del(b) #deletes entire tuple

#counting

print("no of times counted",c.count(2))

print("-------------------------------------------------------------------------------------------------------------------")


#SET

 #creating a set
fruits={"banana","apple","mango","cherry"}
print("created set is ",fruits)

#adding
fruits.add("orange")
print("after adding",fruits)

#remove
fruits.remove("banana")
print("after removing",fruits)

#updation
vegetable={"potato"}
fruits.update(vegetable)
print("after updation",fruits)

print("-------------------------------------------------------------------------------------------------------------------")


#DICTIONARY

#creating dictionary
d={1:"one",2:"two",3:"three"}
print("created dictionary",d)

#adding
d[4]="four"
print(d)

#updating
e={5:"five"}
print(d.update(e))

#pop
print(d.pop(3))

#deletion
del(d)


