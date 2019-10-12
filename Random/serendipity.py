def _printSeq(n):
    arr=list(range(0,n+1))
    step=2
    i=0
    c=0
    while True:
        i=i+step
        print(i)
        if i<n:
            arr.pop(i)
            c+=1
        else:
            break   
        
    print(arr)
    return c
def _printSteps(arr):
    print(arr)
def _pass(arr,step):
    c=0
    i=1
    while True:
        if i<n:
            arr[i]=0
            c+=1
        else:
            break
        i=i+step
    return arr,c
def _serendipity(n):
    arr=list(range(1,n+1))
    count=0
    for i in range(2,n+1):
        out_arr,c=_pass(arr,i)
        count+=c
        _printSteps(out_arr)
    return count
n=int(input("Enter the number of terms: "))
#out=_serendipity(n)
out=_printSeq(n)
print("Number of Steps: ",out)
