import csv
from array import * 

list1=[]
tuple1=()
set1=set()
dictionary1={}
data=[]
array1=("i", [])


with open("assignment2_file.csv") as file:
    reader=csv.reader(file)
    for i in reader: 
        data.append(i)

for z in range(10):
    array1[1].append(data[0][z])

tuple1=tuple(data[1])
list1.extend(data[2])
set1=set(data[3])

for d in range(10):
    dictionary1[data[4][d]]=data[5][d]


with open("assignment2_file.txt", "w") as file2:
    file2.write(str(dictionary1)+"\n")
    file2.write(str(set1)+"\n")
    file2.write(str(list1[:])+"\n")
    file2.write(str(tuple1)+"\n")
    file2.write(str(array1))


with open("assignment2_file.txt",) as file3:
    read=file3.readlines()
    print("Output after reading from the text file:")
    print()
    for i in read:
        print(i)


for search in list1:
    if "fujairah"==i.lower():
        print("Found", search)
    else:
        pass


for search2 in list1:
    if search2=="brown":
        print("Found", search2)
    else:
        pass


for search3 in dictionary1.values():
    if search3.lower()=="data science":
        print("Found, search3")
    else:
        pass



#Now I will be doing indertion sort

def insertion_sort(list1):
    for i in range(1, len(list1)):
        value = list1[i]
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j+1] = value
    return list1

insertion_sort(array1)



def partition(start, end , array):
    pivot_index = start 
    pivot = array[pivot_index]

    while start < end: 
        while start < len(array) and array[start] <= pivot:
            start += 1
        
        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]


    array[end], array[pivot_index] = array[pivot_index], array[end]



# Now comes the quick sort
def mergeSort(tuple1):
    if len(tuple1) > 1:
        mid = len(tuple1) // 2
        left = tuple1[:mid]
        right = tuple1[mid:]

        # Recursive call on each half

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              tuple1[k] = left[i]
              i += 1

            else:
                tuple1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            tuple1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            tuple1[k]=right[j]

            j += 1
            k += 1

mergeSort(tuple1)
print(tuple1)

with open('assignment2_file2.csv') as f: 
    writer = csv.writer(f)
    for i in content:
        temp=[]
        temp.append(i)
        writer.writerow(temp)

