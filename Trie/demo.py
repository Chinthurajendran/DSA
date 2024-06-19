class Trienode:
    def __init__(self):
        self.child ={}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Trienode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Trienode()
            node = node.child[char]
        node.end = True
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.end
    
    def starts_with(self,word):
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return True




trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.starts_with("app")) # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True