class Graph:
    def __init__(self):
        self.dic = {}
    
    def add(self,data):
        self.dic[data] = []
    
    def insert(self,vertix,edge,value):
        if vertix not in self.dic:
            self.add(vertix)
        
        if edge not in self.dic:
            self.add(edge)
        
        self.dic[vertix].append(edge)

        if value:
            self.dic[edge].append(vertix)
    
    def display(self):
        for x in self.dic:
            print(f"{x}: {' '.join(map(str,self.dic[x]))}")


graph = Graph()
graph.insert(4,5,True)
graph.insert(4,56,True)
graph.insert(5,7,False)
graph.display()