allElement = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "


class dfa_node:
    def __init__(self, char=""):
        self.char = char
        self.nextNodeCharList = []
        self.nextNodeList = []
        self.isEndState = False

    def add_next_node(self, node):
        self.nextNodeList.append(node)
        self.nextNodeCharList.append(node.char)

    def is_in_next_node_list(self, char):
        return char in self.nextNodeCharList

    def get_next_node_index(self, char):
        if self.is_in_next_node_list(char):
            return self.nextNodeCharList.index(char)
        return None

    def get_next_node_list(self):
        return self.nextNodeList

    def return_relation_array(self, ancestor=""):
        ancestor = ancestor + self.char
        relationArray = []
        if self.nextNodeList:
            for i in self.nextNodeList:
                relationArray.append((ancestor, ancestor + i.char))
                if i.nextNodeCharList:
                    relationArray.extend(i.return_relation_array(ancestor))
        return relationArray


class Dfa:
    def __init__(self):
        self.root = dfa_node("")
        self.pointingNode = self.root
        self.inTrapState = False

    def initializeDfa(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = pCrawl.get_next_node_index(key[level])
            if index is None:
                pCrawl.add_next_node(dfa_node(char=key[level]))
                index = len(pCrawl.nextNodeList) - 1
            pCrawl = pCrawl.nextNodeList[index]
        pCrawl.isEndState = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = pCrawl.get_next_node_index(key[level])
            if index is None:
                print(key[level] + "Not found")
                return False
            print(key[level] + "Found")
            pCrawl = pCrawl.nextNodeList[index]
        if pCrawl.isEndState:
            print("Found end state. String is valid")
        return pCrawl.isEndState

    def resetDfaState(self):
        self.pointingNode = self.root
        self.inTrapState = False

    def inputNextChar(self, key):
        if len(key) == 1 and key in allElement and self.inTrapState is False:
            pCrawl = self.pointingNode
            index = pCrawl.get_next_node_index(key)
            if index is None:
                self.inTrapState = True
                return None
            self.pointingNode = pCrawl.nextNodeList[index]
            return self.getCurrentState()
        else:
            self.inTrapState = True
            return None

    def getCurrentNodePointingTo(self):
        return self.pointingNode.nextNodeCharList

    def getCurrentState(self):
        if self.inTrapState is False:
            return self.pointingNode.isEndState
        else:
            return None

    def return_relation_array(self):
        return self.root.return_relation_array()
