num=[1,4,54,34,66,78,69,51]
name=['albert','bob','catrine','david']
print (name)
values=[19.5,'albert',876]#can store any datatype in lists
print(values)


num.append(96)#to add a element into the list
print (num)

num.insert(0,12)#add element at the 0th position and value added will be 12
print(num)

num.remove(51)#removed the element '51'
print(num)

num.pop(2)#removes the element in the position 2
print(num)

del num[4:]#deletes all the element after the 4th index value
print(num)

num.extend([23,45,67,89,69])#adds these values to the list
print(num)