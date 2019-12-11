# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #print(f'merged_arr 1:{merged_arr}')
    
    if arrA[0] < arrB[0]:
      merged_arr[:len(arrA)], merged_arr[len(arrA):] = arrA[:], arrB[:]
    else:
      merged_arr[:len(arrB)], merged_arr[len(arrB):] = arrB[:], arrA[:]
    
    #print(f'merged_arr 2:{merged_arr}')
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
    half = len(arr)//2
    arr_a = arr[half:]
    arr_b = arr[:half]
    # recurse until units of 1
    print('ko')
    merge_sort(arr_a)
    print('ok')
    merge_sort(arr_b)
    #print(f'new arr: {arr}')
    # #base case to check for presence of list type
    # if any(isinstance(ele, list) for ele in arr) == False:
    #   return arr
  else:
    print(arr)
    #return arr


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
