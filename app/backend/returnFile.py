import json
from predictFunct import *
from ResponseNotes import *
from query import *
from classify import *

plasticTypes = ["PET_Bottles", "HDPE_Bottles", "PP", "Rigids__3_to_7"]


# returns the recyclability and notes for a plastic identified object
def getReturnPlastic(file, city, state, zipCode):
    print(file)

    # predict type of plastic
    typePlastic = plastic_model_predict(file)

    # get return for the predicted class
    material = typePlastic['predicted_class']

    # get the classification for query
    classifiedPlastic = classify_plastic(material)

    # get the confidence
    if_confident = get_confidence(typePlastic)

    print("/n/n RUNNING PLASTIC")
    

    return getReturnTotal(classifiedPlastic, city, state, zipCode, if_confident)

# returns the recyclability and notes for a other material
def getReturnMaterial(file, city, state, zipCode):
    # tensor flow model predict the material of the item from the picture
    typeOther = material_model_predict(file)

    # finds the predicted class from the return of typeOther (a dictionary)
    material = typeOther['predicted_class']

    # classify for a other material
    classifiedOther = classify_other(material)

    # get the confidence
    if_confident = get_confidence(typeOther)

    print("/n/n RUNNING MATERIAL")

    if classify_plastic(plastic_model_predict(file)['predicted_class']) in plasticTypes and plastic_model_predict['confidence'] >= 0.45:
         return getReturnPlastic(file, city, state, zipCode)
    
    else:
        return getReturnTotal(classifiedOther, city, state, zipCode, if_confident)
    
# returns a json file with if confident, recyclable, and notes data
def getReturnTotal(material, city, state, zipCode, if_confident): 
    isRecyclable = recyclable(zipCode, material)

    # create the ai note
    notes = createNotes((city + ", " + state), material, isRecyclable, if_confident)

    # note if is recyclable
    if isRecyclable:
        isRecyclable = "This Is Recyclable"

    else:
        isRecyclable = "This Is Not Recyclable"

    # return data
    returnData = {
        "ifConfident" : if_confident,
        "isRecyclable" : isRecyclable,
        "notes" : notes
    }

    print("\n\nTESTINGGGG:", isRecyclable, "THE MATERIAL IS:", material)

    with open("../src/finalDataReturn.json", 'w') as json_file:
        finalFile = json.dump(returnData, json_file, indent = 4)

    return finalFile
    


