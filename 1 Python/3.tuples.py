#Tuples (Read only list)
test = [10,20,30]

tuple1 = (3,4,6)
print(type(tuple1))

#access tuple elements by slicing
print(tuple1[0])
print(tuple1[0:5])
print(tuple1[2:3])

#TypeError: 'tuple' object does not support item assignment being it is READ ONLY
tuple1[2] = 100 
print(tuple1)

tuple2 = (10, 20, (40,50), True)
print(tuple2)
print(len(tuple2))