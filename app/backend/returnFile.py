import json
from predictFunct import *
from ResponseNotes import *
from query import *
from classify import *

def getReturnPlastic(file, city, state, zipCode):
    print(file)

    typePlastic = plastic_model_predict(file)
    material = typePlastic['predicted_class']
    classifiedPlastic = classify_plastic(material)

    if_confident = get_confidence(typePlastic)

    return getReturnTotal(classifiedPlastic, city, state, zipCode, if_confident)

def getReturnMaterial(file, city, state, zipCode):
    typeOther = material_model_predict(file)
    material = typeOther['predicted_class']
    classifiedOther = classify_other(material)

    if_confident = get_confidence(typeOther)

    return getReturnTotal(classifiedOther, city, state, zipCode, if_confident)
    
def getReturnTotal(material, city, state, zipCode, if_confident): 
    isRecyclable = recyclable(zipCode, material)
    notes = createNotes((city + ", " + state), material, isRecyclable, if_confident)
    #ask abt this where to put confidence
    returnData = {
        "ifConfident" : if_confident,
        "isRecyclable" : isRecyclable,
        "notes" : notes
    }

    with open("/src/finalDataReturn.json", 'w') as json_file:
        finalFile = json.dump(returnData, json_file, indent = 4)

    return finalFile
    


