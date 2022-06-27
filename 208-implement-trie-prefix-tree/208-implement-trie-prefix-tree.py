class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.is_end = False

class Trie:

    def __init__(self):
        self.base = dict()
        
        
    def insert(self, word: str) -> None:
        if not word[0] in self.base:
            self.base[word[0]] = Node(word[0])
        
        cur_node = self.base[word[0]]
        
        for c in word[1:]:   
            if not c in cur_node.children:
                cur_node.children[c] = Node(c)

            cur_node = cur_node.children[c]
            
        cur_node.is_end = True
        
        

    def search(self, word: str) -> bool:
        
        if not word[0] in self.base:
            return False
        else:
            cur_node = self.base[word[0]]
            
        for c in word[1:]:   
            if not c in cur_node.children:
                return False

            cur_node = cur_node.children[c]
            
        return cur_node.is_end

        
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix[0] in self.base:
            return False
        else:
            cur_node = self.base[prefix[0]]
            
        for c in prefix[1:]:   
            if not c in cur_node.children:
                return False

            cur_node = cur_node.children[c]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)