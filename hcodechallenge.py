def consec(a):
	answer = []

	for i in range(0,len(a)-1):

		

		if i <= len(a)-3:
			first=a[i]
			mid=a[i+1]
			end=a[i+2]


			if mid*3==first+mid+end:

				answer.append(i)

	return answer










