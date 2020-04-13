# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # smallest_index = arr.index(min(arr[i:]))
        
        for index,j in enumerate(arr[current_index:]):
            if j < arr[smallest_index]:
                smallest_index = i + index

        # TO-DO: swap
        temp = arr[i] 
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    clean_pass = False
    while clean_pass == False:
        swap_occured = False
        for i in range(len(arr)-1):
            rhn = arr[i+1]
            current = arr[i]
            if current>rhn:
                temp = rhn
                arr[i+1] = current
                arr[i] = rhn
                swap_occured = True
        if swap_occured == False:
            clean_pass = True
        
    # for every item in arr
        # compare current element with right hand neighbor (rhn)    
        # if rhn is smaller 
            # swap
        # else 
            # do nothing?
        
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # this is the array that stores the counts
    if arr:
        maximum = max(arr)
        if min(arr) < 0:
            return "Error, negative numbers not allowed in Count Sort"
    else:
        return []

    count = [0]*(maximum+1)
    for i in arr:
        count[i] += 1
    output = []
    for index, i in enumerate(count):
        output.extend([index]*i)
    return output

# you could also impliment this with a dictionary.

my_arr = [13,4,6,78,8,2,5,8,3]

a = selection_sort(my_arr)
print(a)

a = bubble_sort(my_arr)
print(a)

a = count_sort(my_arr,max(my_arr))
print(a)
