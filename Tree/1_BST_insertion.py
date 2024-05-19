class Node:
     def __init__(self,key):
          self.key = key
          self.left_child = None
          self.right_child = None
          
     def insert(self,data):
          if self.key is None:
               self.key = data
               return
          
          if self.key > data:
               if self.left_child:
                    self.left_child.insert(data)
               else:   
                    self.left_child = Node(data)
          else:
               if self.right_child:
                    self.right_child.insert(data)
               else:
                    self.right_child = Node(data)
    
     def search(self,data):
          if self.key == data:
               print("Node is found")
               return
          if data < self.key:
               if self.left_child:
                    self.left_child.search(data)
               else:
                    print("Node is empty")
          else:
               if self.right_child:
                    self.right_child.search(data)
               else:
                    print("Node is empty")


     def pre_odrder(self):
          print(self.key,end=" ")
          if self.left_child:
               self.left_child.pre_odrder()
          if self.right_child:
               self.right_child.pre_odrder()

     def in_order(self):
          if self.left_child:
               self.left_child.in_order()
          print(self.key,end=" ")
          if self.right_child:
               self.right_child.in_order()
     
     def post_order(self):
          if self.left_child:
               self.left_child.post_order()
          if self.right_child:
               self.right_child.post_order()
          print(self.key,end=" ")


     def delete(self,data):
          if self.key is None:
               print("Tree is empty")
               return
          if data < self.key:
               if self.left_child:
                    self.left_child = self.left_child.delete(data)
               else:
                    print("Node is not given")
          elif data > self.key:
               if self.right_child:
                    self.right_child = self.right_child.delete(data)
               else:
                   print("Node is not given") 
          else:
               if self.left_child is None:
                    temp = self.right_child
                    self = None
                    return temp
               if self.right_child is None:
                    temp = self.left_child
                    self = None
                    return temp
               node = self.right_child
               while node.left_child:
                    node = node.left_child
               self.key = node.key
               self.right_child = self.right_child.delete(data)
          return self
     
     def min_node(self):
          current = self
          while current.left_child:
               current = current.left_child
          print(current.key)

     def max_node(self):
          current = self
          while current.right_child:
               current = current.right_child
          print(current.key)





        

data  = Node(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
     data.insert(i)

data.search(3)
print("Pre_odrder")
data.pre_odrder()
print("\nIn_order")
data.in_order()
print("\nPost_order")
data.post_order()
print()
data.min_node()
print()
data.max_node()