#given an array of unsorted positive integers:
a = [1,2,3,5,10,9,8,9,10,11,7]

def answer():

	#list that will return indices where runs begin:
	answer = []

	#range of indices that function will be conducted within:
	for i in range(0,len(a)-1):

		
		#ensures the function will have at least 3 numbers
		#to work with toward the end of the given array:
		if i <= len(a)-3:

			#finds runs of 3 consecutive integers:
			first=a[i]
			mid=a[i+1]
			end=a[i+2]

			#validates run;
			#mid element * total amount of elements will always equal sum of all elements
			#in a run of consecutive integers regardless of
			#how many elements contained in list or ascending/descending:
			if mid*3==first+mid+end:

				#adds inidices of start of run to a list:
				answer.append(i)

	print a
	print answer

answer()










