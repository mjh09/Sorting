# TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr)-1):
#         cur_index = i
#         # smallest_index = cur_index
#         # # TO-DO: find next smallest element
#         # # (hint, can do in 3 loc) 
#         smallest_index = arr.index(min(arr[cur_index+1:]))     



#         # TO-DO: swap
#         if arr[cur_index]< arr[smallest_index]:
#             pass
#         else:
#             arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
            
        
#     return arr

def selection_sort( arr ):
    c=1
    while True:
        c=0
        # loop through n-1 elements
        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
        
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc) 
            for j in range(i+1, len(arr)):
                if arr[cur_index] > arr[j]:
                    smallest_index = j
                    c+=1     

            # TO-DO: swap
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    
    
        if c ==0:
            break

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 1
    while True:
        i = 0
        for idx in range(len(arr)-1):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                i+=1

        if i == 0:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr