import json
import modules.extension as extension
import modules.myLogger as myLogger


def parse(targetFile):
    myLogger.configFile("../logs/extensionBuilder.log", "debug")
    with open(targetFile) as f:
        targetData = json.load(f)
    targetDataList = list()
    for x in targetData:
        myLogger.debug(f'[EXTENSION BUILDER]: Created Target Object for {targetData[x]["FULL_TARGET_URL"]}')
        targetDataList.append(extension.ExtensionInstance(targetData[x]["FULL_TARGET_URL"],
                                                  targetData[x]["FILTERS"], targetData[x]["THREADS"],
                                                  targetData[x]["PRIORITY_LEVEL"]))
    return targetDataList
