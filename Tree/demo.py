     def second_largest(self):
        
        if not self.right:
            if self.left:
                print(self.left.key)
            else:
                return None
        if not self.right.left and not self.right.right:
            return self.key
        return self.right.second_largest()
    
     def second_samllest(self):
        
        if not self.left:
            if self.right:
                print(self.right.key)
            else:
                return None
        
        if not self.left.left and not self.left.right:
            return self.key
        
        return self.left.second_samllest()