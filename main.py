import src.trie as trie
import src.graph as graph
import src.source as fileManagement

relationArrayList = fileManagement.readFile("data/trie.txt")
# t = trie.Trie()
relationArray = []
for key in relationArrayList:
    key = key.strip("()")
    tempList = list(map(str, key.split("', '")))
    for index, data in enumerate(tempList):
        tempList[index] = str(data.strip("'"))
    relationArray.append(tuple(tempList))

# test = ["('', 'B')", "('C 1', 'C 13')", "('C ', 'C 1')"]
# for key in test:
#     key = key.strip("()")
#     tempList = list(map(str, key.split("', '")))
#     for index, data in enumerate(tempList):
#         tempList[index] = str(data.strip("'"))
#     relationArray.append(tuple(tempList))
# print(relationArray)

print("Finished reading data")
graph.drawGraph(relationArray)
