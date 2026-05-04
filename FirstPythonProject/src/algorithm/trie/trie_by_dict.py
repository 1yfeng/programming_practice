class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_vaild = False
        self.val = None

class Trie:
    def __init__(self):
        self.root = {}
    
    def get_root(self):
        return self.root
    
    def insert(self, word: str):
        node = self.root
        for i in word:
            if i not in node:
                node[i] = TrieNode()
            node = node[i].child
        node.is_vaild = True
        
                
