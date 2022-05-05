import src.source as fileManagement
import os

cwd = os.getcwd()


def test_readFile_absolutePath():
    assert fileManagement.readFile(cwd + "\\sample\\test.txt")[0] == "Hello World"


def test_readFile_relativePath():
    assert fileManagement.readFile("sample/test.txt")[0] == "Hello World"


def test_readJson():
    assert fileManagement.readJson("sample/test.json")[0]["test"] == 1


def test_writeFile():
    outputFile = "sample/test_out.txt"
    outputData = "Hello World"
    fileManagement.writeFile(outputFile, outputData)
    assert fileManagement.readFile(outputFile)[0] == outputData
    if os.path.exists(outputFile):
        os.remove(outputFile)


def test_writeFile2():
    outputFile = "sample/test_out.txt"
    outputData = ["Hello World", "Hello World2"]
    fileManagement.writeFile(outputFile, "\n".join(outputData))
    assert fileManagement.readFile(outputFile) == outputData
    if os.path.exists(outputFile):
        os.remove(outputFile)


def test_writeFileLines():
    outputFile = "sample/test_out.txt"
    outputData = ["Hello World", "Hello World2"]
    fileManagement.writeFileLines(outputFile, outputData)
    assert fileManagement.readFile(outputFile)[0] == "".join(outputData)
    if os.path.exists(outputFile):
        os.remove(outputFile)



