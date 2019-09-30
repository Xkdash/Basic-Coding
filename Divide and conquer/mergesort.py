def _mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        _mergeSort(L)
        _mergeSort(R)

        i=j=k=0
        while i<len(L) and j< len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
def _input():
    n=int(input("Enter the number of elements: "))
    A=[]
    for i in range(0,n):
        A.append(int(input("val"+str(i)+": ")))
    return A
def _output(A):
    print("The output Array: ")
    for i in range(0,len(A)):
        print(A[i])
def _main():
    array_in=_input()
    _mergeSort(array_in)
    _output(array_in)
if __name__ == '__main__':
    _main()
