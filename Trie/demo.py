class TrieNode:
    def __init__(self):
        self.children  = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end
    
    def starts_with(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.starts_with("app")) # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True