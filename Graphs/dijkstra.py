class Graph:
    def __init__(self,Vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
    
def _shortestPath(G,s)
    

def _input():
    
    G=Graph(8)
    G.graph=[[0,3,6,0,9,0,9,0],[3,0,2,0,0,0,0,7],[6,2,0,11,13,0,0,0],[11,0,0,0,0,10,0,14],[9,0,13,0,0,0,7,0],[0,0,0,10,0,0,0,5],[9,0,0,0,7,0,0,8],[0,7,0,14,0,5,8,0]]
    src=int(input("Enter a source Node: "))
    return G,src
def _output(G):
    print("The output Array: ")
    for i in range(0,len(A)):
        print(A[i])
def _main():
    G,src=_input()
    path=_shortestPath(G,src)
    _output(path)
if __name__ == '__main__':
    _main()
