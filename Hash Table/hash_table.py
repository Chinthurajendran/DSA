class hash_table:
    def __init__(self,size):
        self.size = size
        self.table = [None for i in range(self.size)]
        print(self.table)
    
    # def get_hash(self,value):
    #     return value%self.size
    
    def get_hash(self,key):
        data = 0
        for char in key:
            data += ord(char)
        return data%self.size
    
    # def add(self,value):
    #     index= self.get_hash(value)
    #     self.table[index] = value

    #     print(self.table)

    def add(self,key,value):
        index = self.get_hash(key)
        self.table[index] = value
        
    def get(self,value):
        index = self.get_hash(value)
        return self.table[index] 

    def display_pairs(self):
        print("Key-Value Pairs:")
        for index, item in enumerate(self.table):
            print(f"{index}: {item}")
    


info = hash_table(10)
# info.add(5)
info.add('chinthu',5)
print(info.get('chinthu'))
info.display_pairs()