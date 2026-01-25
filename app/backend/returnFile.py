import json
from predictFunct import *
from responseNotes import *
from query import *
from classify import *

def getReturnPlastic(file):
    typePlastic = plastic_model_predict(file.filename)
    classifiedPlastic = classify_plastic(typePlastic)

    return getReturnTotal(classifiedPlastic)

def getReturnMaterial(file):
    typeOther = material_model_predict(file.filename)
    classifiedOther = classify_other(typeOther)

    return getReturnTotal(classifiedOther)
    
def getReturnTotal(material): 
    # query's connect
    connect()

    # find the location
    with open('location.json', 'r') as file:
        data = json.load(file)

    # Accessing data like a Python dictionary
    zipCode = data['zip_code']
    city = data['city']
    state = data['state']

    isRecyclable = recyclable(zipCode, material)
    notes = createNotes((city + ", " + state), material, isRecyclable)

    returnData = {
        "isRecyclable" : isRecyclable,
        "notes" : notes
    }

    with open("finalDataReturn", 'w') as json_file:
        finalFile = json.dump(returnData, json_file, indent = 4)

    return finalFile
    


