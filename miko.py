
'''
A.   Write a function that takes two numbers as parameters
returns a list of n smallest odd integers greater than or equal to start, in ascending order.
	Example:
                       Myfunc(4,10)

	Output:
	[5,7,9,11,13,15,17,19,21,23]

'''



def Myfunc(a, b):


    # if a is even
    if a % 2 == 0:
        a = a + 1


# replace a = a + 1 UP with a = a + 0 DOWN
    # for evens

    # if a is odd
    elif a % 2 == 1:
        a = a + 0

    list=[]

    for i in range(b):
        list.append(a)
        a = a + 2

    print(list)


Myfunc(14, 10)




print("mikoooooooooooooooo git push")












'''
B.   Create two functions one to filter the word ‘perscholas’ from vowels letters and the 
    second function to filter the word ‘perscholas’ from consonants
	
	Examples:
	vowelfilter(“perscholas”)
	output:
	prschls
	
	consonantsfilter(“perscholas”)
	output:
	eoa
	
	'''







def vowelfilter(b):

    vowels=['a', 'e', 'i', 'o', 'u']

    for i in b.lower():
        if i in vowels:
            b = b.replace(i, "")

    return b

vowelfilter("perscholas")







def consonantsfilter(a):
    vowels = ['a', 'e', 'i', 'o', 'u']

    returnstring = ""
    for i in a.lower():
        if i in vowels:
           returnstring = returnstring + i

    return returnstring


consonantsfilter("perscholas")

