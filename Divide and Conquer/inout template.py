

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
