import modules.extensionBuilder as extensionBuilder

# just here to get the extensionBuilder worked out

setOfTargets = extensionBuilder.parse("./targets/exampleTargetBatch.json")
print('[TARGETS]:')
for x in setOfTargets:
    print(x)
