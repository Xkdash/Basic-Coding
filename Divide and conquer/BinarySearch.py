def _binarySearchConfirm(arr,item):
    mid=len(arr)//2
    if arr[mid]==item:
        print("Item found: ",item)
    elif item<arr[mid]:
        _binarySearchConfirm(arr[:mid],item)
    elif item>arr[mid]:
        _binarySearchConfirm(arr[mid+1:],item)
    else :return
def _binarySearchIndex(arr,item,l,r):
    if r>=l:
        mid=((r-l)//2)+1
        if arr[mid]==item:
            print("Found at", mid)
        elif arr[mid]>item:
            _binarySearchIndex(arr,item,l,mid-1)
        else:
            _binarySearchIndex(arr,item,mid+1,r)
    else:
        print("Not found")
def _input():
    n=int(input("Enter the number of elements: "))
    A=[]
    for i in range(0,n):
        A.append(int(input("val"+str(i)+": ")))
    item=int(input("Enter the number to search: "))
    return A,item
def _main():
    array_in,item =_input()
    array_in.sort()
    #_binarySearchConfirm(array_in,item)
    _binarySearchIndex(array_in,item,0,len(array_in)-1)
if __name__ == '__main__':
    _main()
