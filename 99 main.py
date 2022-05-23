import src.trie as trie
import src.graph as graph
import src.source as fileManagement

dictionaryList = fileManagement.readFile("data\ListOfPlace.txt")
t = trie.Trie()
for key in dictionaryList:
    t.insert(key)
relationArrayPre = t.returnRelationArray()

# test = ["('', 'B')", "('C 1', 'C 13')", "('C ', 'C 1')"]
# for key in test:
#     key = key.strip("()")
#     tempList = list(map(str, key.split("', '")))
#     for index, data in enumerate(tempList):
#         tempList[index] = str(data.strip("'"))
#     relationArray.append(tuple(tempList))
relationArray = []

for key in relationArrayPre:
    if key[0] == '':
        relationArray.append(('StartPoint', key[1]))
    else:
        relationArray.append(key)

print(len(relationArray))

print("Finished reading data")
graph.drawGraph(relationArray)
