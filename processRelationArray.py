import src.trie as trie
import src.source as fileManagement

dictionaryList = fileManagement.readFile("data/extractedData.txt")
t = trie.Trie()
for key in dictionaryList:
    t.insert(key)
fileManagement.writeFile("data/trie.txt", "\n".join(map(str, t.returnRelationArray())))
