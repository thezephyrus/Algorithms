# Bucket Sort - Time complexity - > O(n)
'''
***********
Bucket Sort
***********
Suppose we need to sort an array of positive integers {3,11,2,9,1,5}. A bucket sort works as follows: create an array of size 11
Then, go through the input array and place integer 3 into a second array at index 3, integer 11 at index 11 and so on.
We will end up with a sorted list in the second array.

Suppose we are sorting a large number of local phone numbers, for example, all residential phone numbers in the 412 area code region
(about 1 million) We sort the numbers without use of comparisons in the following way. Create an a bit array of size 107.
It takes about 1Mb. Set all bits to 0. For each phone number turn-on the bit indexed by that phone number.
Finally, walk through the array and for each bit 1 record its index, which is a phone number.

We immediately see two drawbacks to this sorting algorithm. Firstly, we must know how to handle duplicates.
Secondly, we must know the maximum value in the unsorted array.. Thirdly, we must have enough memory -
it may be impossible to declare an array large enough on some systems.

The first problem is solved by using linked lists, attached to each array index. All duplicates for that bucket
will be stored in the list. Another possible solution is to have a counter.
As an example let us sort 3, 2, 4, 2, 3, 5. We start with an array of 5 counters set to zero.

0 1 2 3 4 5  
0 0 0 0 0 0
Moving through the array we increment counters:
0 1 2 3 4 5  
0 0 2 2 1 1
Next,we simply read off the number of each occurrence: 2 2 3 3 4 5.


Source context: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html

'''


import numpy

myArray = numpy.random.randint(0,100,size=100) # Creating a size of 100 to have 100 indices
#myArray = [3,3,3,2,0]
print('Input Array:')
print(myArray)

#resultArray = [0] * len(myArray)
captureDuplicate = [0] * len(myArray)

resultArray=[{}for i in range(len(myArray))] # Initializing an empty Array to avoid issue with number 0 and index 0

# Pick and place the number in the index of result array &
# increment if encountering duplicate values in the duplicates array

for i in range(0,len(myArray)):
    if captureDuplicate[myArray[i]] == 0 and myArray[i] != 0:
        resultArray[myArray[i]]=myArray[i]
        captureDuplicate[myArray[i]]=1
    else:
        captureDuplicate[myArray[i]] += 1
        resultArray[myArray[i]]=myArray[i]
        
print('Final Sorted Result')
print(resultArray)
print('\nCount of Occurences')

for x in range(0,len(captureDuplicate)):
    format_list=[x,captureDuplicate[x]]
    if captureDuplicate[x] != 0:
        print('\nValue:')
        print(x)
        print('Count:')
        print(captureDuplicate[x])

print('Bucket Sort Complete!!!')
