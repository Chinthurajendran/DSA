class Graph:
    def __init__(self):
        self.dict ={}
    
    def add_vertix(self,data):
        self.dict[data] = []
    
    def insert(self,vertix,edage,value):

        if vertix not in self.dict:
            self.add_vertix(vertix)
        
        if edage not in self.dict:
            self.add_vertix(edage)
        self.dict[vertix].append(edage)

        if value:
            self.dict[edage].append(vertix)
    
    def display(self):
        for x in self.dict:
            print(f"{x}:{" ".join(map(str,self.dict[x]))}")

        


graph = Graph()
graph.insert(4,5,True)
graph.insert(4,56,True)
graph.insert(5,7,False)
graph.display()