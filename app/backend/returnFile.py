import json
from predictFunct import *
from responseNotes import *
from query import *
from classify import *

def getReturnPlastic(file, city, state, zipCode):
    typePlastic = plastic_model_predict(file.filename)
    classifiedPlastic = classify_plastic(typePlastic)

    return getReturnTotal(classifiedPlastic, city, state, zipCode)

def getReturnMaterial(file, city, state, zipCode):
    typeOther = material_model_predict(file.filename)
    classifiedOther = classify_other(typeOther, city, state, zipCode)

    return getReturnTotal(classifiedOther)
    
def getReturnTotal(material, city, state, zipCode): 
    # query's connect
    connect()

    isRecyclable = recyclable(zipCode, material)
    notes = createNotes((city + ", " + state), material, isRecyclable)

    returnData = {
        "isRecyclable" : isRecyclable,
        "notes" : notes
    }

    with open("finalDataReturn", 'w') as json_file:
        finalFile = json.dump(returnData, json_file, indent = 4)

    return finalFile
    


