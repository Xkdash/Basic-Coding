def _uniqueArray(arr):
    s=set()
    for i in range(0,len(arr)):
        s.add(arr[i])
    return s

def _input():
    n=int(input("Enter the number of elements: "))
    A=[]
    for i in range(0,n):
        A.append(int(input("val"+str(i)+": ")))
    return A
def _output(A):
    print("The output Set: ")
    for s in A:
        print(s)
def _main():
    array_in=_input()
    out_array=_uniqueArray(array_in)
    _output(out_array)
if __name__ == '__main__':
    _main()
