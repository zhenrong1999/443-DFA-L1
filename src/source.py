import json


def readFile(name):
    file = open(name, 'r', encoding='utf-8')
    new_lst = []
    for line in file.readlines():
        new_lst.append(line.strip('\n'))
    return new_lst


def readJson(name):
    jsonArray = []
    lines = readFile(name)
    for line in lines:
        jsonArray.append(json.loads(line))
    return jsonArray


def writeFile(name, data):
    file = open(name, 'w', encoding='utf-8')
    file.write(data)
    file.close()


def writeFileLines(name, data):
    file = open(name, 'w', encoding='utf-8')
    file.writelines(data)
    file.close()
