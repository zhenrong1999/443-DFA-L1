import src.DFA as DFA
import src.source as fileManagement

dictionaryList = fileManagement.readFile("data\ListOfPlace.txt")
t = DFA.Dfa()
for key in dictionaryList:
    t.initializeDfaState(key)

# UI for search input
while True:
    searchInput = input("Enter search input: ")
    if searchInput == "":
        break
    t.initializeSearch()
    for char in searchInput:
        print(char + ": ", t.insertNextChar(char))
