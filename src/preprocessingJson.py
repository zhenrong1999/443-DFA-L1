from src.source import readJson
import re


def isEnglishCharacters(word):
    return re.match('^[a-zA-Z0-9 ]*$', word) is not None


def extractJsonFile(jsonFile):
    extractedData = []
    for i in readJson(jsonFile):
        item = i['norm_name']
        if(isEnglishCharacters(item)):
            extractedData.append(item.strip())
    return list(dict.fromkeys(extractedData))
