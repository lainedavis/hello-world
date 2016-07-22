
def array_loop(array):
	for element in array:
		print(element)

array = ['a','b','c','d','e']

array_loop(array)

# best way to loop through elements and add to new array
fast_array = [each+'test' for each in array]
print(fast_array)
