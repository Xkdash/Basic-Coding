class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def _binaryTree(arr):
    if not arr:
        return None
    mid=len(arr)//2
    root=Node(arr[mid])
    root.left=_binaryTree(arr[:mid])
    root.right=_binaryTree(arr[mid+1:])
    return root
def _preOrder(node):
    if not node:
        return
    print(node.data)
    _preOrder(node.left)
    _preOrder(node.right)

def _postOrder(node):
    if not node:
        return
    _postOrder(node.left)
    _postOrder(node.right)
    print(node.data)
def _inOrder(node):
    if not node:
        return
    _inOrder(node.left)
    print(node.data)
    _inOrder(node.right)

def _levelOrder(node):
    A=[]
    A.append(node)
    while True:
        item=A.pop(0)
        print(item.data)
        if not item.left == None:
            A.append(item.left)
        if not item.right == None:
            A.append(item.right)
        if len(A)==0:
            break
        

            
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
    array_in.sort()
    root=_binaryTree(array_in)
    _output(array_in)
    print("PreOrder: ")
    _preOrder(root)
    print("InOrder: ")
    _inOrder(root)
    print("PostOrder: ")
    _postOrder(root)
    print("LevelOrder: ")
    _levelOrder(root)
if __name__ == '__main__':
    _main()
