import src.trie as trie


class Test_TrieNode_1:
    t = trie.TrieNode()
    t2 = trie.TrieNode(char="t")
    t.addChildrenNode(t2)

    def test_ChildrenNode_Exists(self):
        assert self.t.isInChildrenList("t") is True

    def test_addChildrenNode_NonExists(self):
        assert self.t.isInChildrenList("a") is False

    def test_returnRelationArray(self):
        assert self.t.returnRelationArray() == [("", "t")]


class Test_Trie:
    t = trie.Trie()
    t.insert("test")
    t.insert("test2")

    def test_search_Exists(self):
        assert self.t.search("test") is True

    def test_search_NonExists(self):
        assert self.t.search("test3") is False

    def test_returnRelationArray(self):
        listResult = self.t.returnRelationArray()
        listResult.reverse()
        assert listResult == [
            ("", "t"),
            ("t", "te"),
            ("te", "tes"),
            ("tes", "test"),
            ("test", "test2"),
        ]
