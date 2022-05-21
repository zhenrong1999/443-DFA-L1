# ref: https://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode:

    # Trie node class
    def __init__(self, char=""):
        self.char = char
        self.childrenList = []
        self.childrenNode = []

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

    def addChildrenNode(self, node):
        self.childrenNode.append(node)
        self.childrenList.append(node.char)

    def isInChildrenList(self, char):
        return char in self.childrenList

    def getChildrenNodeIndex(self, char):
        if self.isInChildrenList(char):
            return self.childrenList.index(char)
        return None

    def returnRelationArray(self, ancestor=""):
        ancestor = ancestor + self.char
        relationArray = []
        if self.childrenNode != []:
            for i in self.childrenNode:
                if i.childrenNode != []:
                    relationArray.extend(i.returnRelationArray(ancestor))
                relationArray.append((ancestor, ancestor + i.char))
        return relationArray


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode("")

    def getNode(self, char=""):

        # Returns new trie node (initialized to NULLs)
        return TrieNode(char=char)

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = pCrawl.getChildrenNodeIndex(key[level])
            # if current character is not present
            if index is None:
                pCrawl.addChildrenNode(self.getNode(char=key[level]))
                index = len(pCrawl.childrenList) - 1
            pCrawl = pCrawl.childrenNode[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = pCrawl.getChildrenNodeIndex(key[level])
            if index is None:
                return False
            pCrawl = pCrawl.childrenNode[index]

        return pCrawl.isEndOfWord

    def returnRelationArray(self):
        return self.root.returnRelationArray()
