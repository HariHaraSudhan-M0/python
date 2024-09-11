data={'a':'albert','b':'singh','c':'peter','d':'son'}#key value pair and should be immutable
print(data['a'])
#get() to fetch the values
#pop() to remove the values
print("using get() : ",data.get(2))

key=['python','javascrtipt','java']
value=['flask','node','spring']
#2 lists need to merge as a dictionary
datas=dict(zip(key,value))#zip function adds the 2 lists and dict is to make the 'datas' as dictionary
print(datas)

# delete a value in the dictionary
del datas['python']
print(datas)
del data['a']
print(data)