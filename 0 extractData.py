import src.preprocessingJson as workOnJson
import src.source as fileManagement

f = workOnJson.extractJsonFile(
    "data/WikidataNE_20170320_Organizations_NECKAR_1_0.json"
) + workOnJson.extractJsonFile("data/WikidataNE_20170320_Locations_NECKAR_1_0.json")
print(len(f))
f.sort()
fileManagement.writeFile("data/extractedData.txt", "\n".join(f))
