# create a method that takes two arrays and returns the common elements in a new arrays


a=[2,3,4,5,6,7,8,9]
b=[1,3,5,7,9,10,11,12]

# using for loop and if conditional
# for num in a:
# 	if num in b:
# 		print num	

# using set and intersection
print (set(a).intersection(b))
