
def _editDistance(S1,S2,n1,n2):
    if n1==0:
        return n2
    if n2==0:
        return n1
    if S1[n1-1]==S2[n2-1] :
        return _editDistance(S1,S2,n1-1,n2-1)
    return 1+ min(_editDistance(S1,S2,n1-1,n2),_editDistance(S1,S2,n1,n2-1),_editDistance(S1,S2,n1-1,n2-1)) #insert,delete,replace

def _input():
    S1=input("Enter the First String: ")
    S2=input("Enter the Second String: ")
    return S1,S2

def _output(n):
    print("The number of operations are: ",n)
def _main():
    S1,S2=_input()
    dist=_editDistance(S1,S2,len(S1),len(S2))
    _output(dist)
if __name__ == '__main__':
    _main()
