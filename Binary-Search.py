def binarySearch(arr,start_position,end_position,key_element):

    middle_position=(start_position+end_position)//2
    if arr[middle_position]==key_element:
        return middle_position
    elif arr[middle_position]>key_element:
        return binarySearch(arr,start_position,middle_position-1,key_element)
    else:
        return binarySearch(arr,middle_position+1,end_position,key_element)

arr=list(map(int,input("Enter the elements: ").split()))
key=int(input("Enter the search element: "))
print(binarySearch(arr,0,len(arr),key))