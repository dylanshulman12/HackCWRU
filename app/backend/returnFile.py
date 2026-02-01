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

    print("/n/n RUNING PLASTIC")

    return getReturnTotal(classifiedPlastic, city, state, zipCode, if_confident)

def getReturnMaterial(file, city, state, zipCode):
    typeOther = material_model_predict(file)
    material = typeOther['predicted_class']
    classifiedOther = classify_other(material)

    if_confident = get_confidence(typeOther)

    print("/n/n RUNING MATERIAL")

    if material == "Plastic" or material == "Rigids__3_to_7":
        return getReturnPlastic(file, city, state, zipCode)
    
    else:
        return getReturnTotal(classifiedOther, city, state, zipCode, if_confident)
    
def getReturnTotal(material, city, state, zipCode, if_confident): 
    isRecyclable = recyclable(zipCode, material)
    notes = createNotes((city + ", " + state), material, isRecyclable, if_confident)
    #ask abt this where to put confidence
    if isRecyclable:
        isRecyclable = "This Is Recyclable"

    else:
        isRecyclable = "This Is Not Recyclable"

    returnData = {
        "ifConfident" : if_confident,
        "isRecyclable" : isRecyclable,
        "notes" : notes
    }

    print("\n\nTESTINGGGG:", isRecyclable, "THE MATERIAL IS:", material)

    with open("../src/finalDataReturn.json", 'w') as json_file:
        finalFile = json.dump(returnData, json_file, indent = 4)

    return finalFile
    


