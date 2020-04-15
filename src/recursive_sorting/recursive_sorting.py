import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = []
        larger = []
        for i in arr[1:]:
            if i <= pivot:
                smaller.append(i)
            else:
                larger.append(i)
        return quicksort(smaller) + [pivot] + quicksort(larger)

def shuff(n=10):
    return [random.randint(0,n) for i in range(n)]

# print(shuff(16))
# a = shuff(10)
# print(a)
# print(quicksort(a))

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # we need a loop that has n iterations 
    # where n is len(a) + len(b)
    elements = len(arrA) + len(arrB)
    merged_arr = []

    for i in range(elements):  
        if len(arrA) == 0 or len(arrB) == 0:
            break  
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    merged_arr.extend(arrA)
    merged_arr.extend(arrB)
    return merged_arr

    # try implimenting with pointers to the array instead

    # try implimenting with initial array declaration instead of 
    # 

def merge2(arrA,arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0]*elements

    for i in range(elements):  
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
    return merged_arr


a = [1,4,5]
b = [2,3,6]
print(merge2(a,b))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    
    # Base case:
    # if the array is 1 or 0 items large return that item

    if len(arr) <= 1:
        return arr

    # split the array 
    half = len(arr)//2
    left = arr[:half]
    right = arr[half:]

    # call merge_sort on the left and right sides
    a = merge_sort(left) 
    b = merge_sort(right)

    # merge the left and right sides 
    output = merge2(a,b)

    return output
    # last few steps can be written as 
    # return merge(merge_sort(left),merge_sort(right))

# I wonder if you can have a ratio of the merges to the sorts
# write a program so that the ratio of splitting to ordering is preserved
# don't go max recusrion depth, but at some point start doing some other iterative sorting strategy?

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr)
print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
