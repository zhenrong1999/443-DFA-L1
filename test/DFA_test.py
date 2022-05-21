import src.DFA as DFA


class Test_dfa_node_1:
    t = DFA.dfa_node()
    t2 = DFA.dfa_node(char="t")
    t.add_next_node(t2)

    def test_is_in_next_node_list(self):
        assert self.t.is_in_next_node_list("t") is True

    def test_is_in_next_node_list2(self):
        assert self.t.is_in_next_node_list("a") is False

    def test_return_relation_array(self):
        assert self.t.return_relation_array() == [("", "t")]


class Test_Dfa:
    t = DFA.Dfa()
    t.initializeDfaState("test")
    t.initializeDfaState("testa")

    def test_search_Exists(self):
        assert self.t.search("test") is True

    def test_search_NonExists(self):
        assert self.t.search("test3") is False

    def test_search_Char_by_Char(self):
        self.t.initializeSearch()
        for i in "test":
            self.t.insertNextChar(i)
        assert self.t.getCurrentState() is True

    def test_search_Char_by_Char2(self):
        self.t.initializeSearch()
        for i in "tes":
            self.t.insertNextChar(i)
        assert self.t.insertNextChar("t") is True

    def test_search_Char_by_Char3(self):
        self.t.initializeSearch()
        for i in "tes":
            self.t.insertNextChar(i)
        assert self.t.insertNextChar(" ") is None

    def test_search_Char_by_Char4(self):
        self.t.initializeSearch()
        for i in "tesxx":
            self.t.insertNextChar(i)
        assert self.t.insertNextChar(" ") is None

    # def test_return_relation_array(self):
    #     listResult = self.t.return_relation_array()
    #     # listResult.reverse()
    #     assert listResult == [
    #         ("", "t"),
    #         ("t", "te"),
    #         ("te", "tes"),
    #         ("tes", "test"),
    #         ("test", "test2"),
    #     ]
