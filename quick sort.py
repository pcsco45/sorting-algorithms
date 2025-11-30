def quickSort(alist):
   quickSortCaller(alist,0,len(alist)-1)

def quickSortCaller(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortCaller(alist,first,splitpoint-1)
       quickSortCaller(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

alist = [11, 13, 20, 5, 2, 1, 21, 6, 7, 67, 6]
quickSort(alist)
print(alist)

