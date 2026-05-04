class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_vaild = False
        self.val = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    def insert(self, word: str):
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = TrieNode()
            node = node.child[i]
        node.is_vaild = True
        
                
