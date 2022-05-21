import src.trie as trie
import src.source as fileManagement

dictionaryList = fileManagement.readFile("sample\ListOfPlace.txt")
t = trie.Trie()
for key in dictionaryList:
    t.insert(key)
fileManagement.writeFile(
    "data/simplifiedTrie.txt", "\n".join(map(str, t.returnRelationArray()))
)
