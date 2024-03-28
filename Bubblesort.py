input_arr = [6,3,1,5,0]

def bubble_sort(arr) : 
    n = len(arr)

    for i in range (n): #0,1,2,3,4,5
        for k in range (0,n-1):
            element = arr[k]
            elementright= arr[k+1]
            print ('elementr:',element)
            print ('elementright:',elementright)
            print('================================')
# swap
            if element > elementright:
                arr[k] = elementright
                arr[k+1] = element
                print('swapped:', arr)
                print('================================')

    print('final:', arr)

bubble_sort(input_arr)