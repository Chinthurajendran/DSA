class Node:
     def __init__(self,key):
          self.key = key
          self.left = None
          self.right = None
     def insert(self,data):
          if self.key is None:
               self.key = data
               return
          if self.key > data:
               if self.left:
                    self.left.insert(data)
               else:
                    self.left = Node(data)
          else:
               if self.right:
                    self.right.insert(data)
               else:
                    self.left = Node(data)
        
     def delete(self,data):
          if self.key is None:
               print("Tree is empty")
               return
          if self.key > data:
               if self.left:
                    self.left = self.left.delete(data)
               else:
                    print("Node is not given")
          elif self.key < data:
               if self.right:
                    self.right = self.right.delete(data)
               else:
                    print("Node is not given")
          else:
               if self.left is None:
                    temp = self.right
                    self = None
                    return temp
               if self.right is None:
                    temp = self.left
                    self = None
                    return temp
               node = self.right
               while node.left:
                    node = node.left
               self.key = node.data
               self.right = self.right.delete(data)
          return self
     
     def search(self,data):
          if self.key ==  data:
               print("Data is found")
               return
          if self.key > data:
               if self.left:
                    self.left.search(data)
               else:
                    print("Node is not given")
          else:
               if self.right:
                    self.right.search(data)
               else:
                    print("Node is not given")
     
     def pre_order(self):
          print(self.key,end=" ")
          if self.left:
               self.left.pre_order()
          if self.right:
               self.right.pre_order()
     def in_order(self):
          if self.left:
               self.left.in_order()
          print(self.key,end=" ")
          if self.right:
               self.right.in_order()
    
     def post_order(self):
          if self.left:
               self.left.post_order()
          if self.right:
               self.right.post_order()
          print(self.key,end=" ")

     def min_node(self):
          current  = self
          while current.left:
               current = current.left
          print(current.key)
    
     def max_node(self):
          current = self
          while current.right:
               current = current.right
          print(current.key)
        
     
            




    
          
          
          

data = Node(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
     data.insert(i)

data.search(3)
print("Pre_odrder")
data.pre_order()

print("\nIn_order")
data.in_order()

# data.delete(98)

print("\nPost_order")
data.post_order()
print()

data.min_node()
print()
data.max_node()