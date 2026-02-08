#take tensor flow output and change it to database fields, ensure confidence
#eventually delete class, sync database and tensorflow names of fields

#plastics with resin code
#convert tensor flow text field to database table names
def classify_plastic(material):
    if material == "1_polyethylene_PET":
        mat_str = "PET_Bottles"
    elif material == "2_high_density_polyethylene_PE-HD":
        mat_str = "HDPE_Bottles"
    elif material == "5_polypropylene_PP":
        mat_str = "PP"
    elif (material == "3_polyvinylchloride_PVC"
          or material == "4_low_density_polyethylene_PE-LD" 
          or material == "6_polystyrene_PS"
          or material == "7_other_resins"):
        mat_str = "Rigids__3_to_7"
    else:
        mat_str = ""
    return mat_str

#other items
#convert tensor flow text field to database table names
def classify_other(item):
    if (item == "Metal"):
        mat_str = "Aluminum"
    elif (item == "Cardboard"):
        mat_str = "Cardboard_Boxboard"
    elif (item == "Plastic"):
        mat_str = "Rigids__3_to_7"
    elif (item == "Glass"):
        mat_str = "Glass"
    elif (item == "Paper"):
        mat_str = "Paper"
    else:
        mat_str = ""
    return mat_str

#if confidence is over 0.45 LLM is confident in result, return true
def get_confidence(dict):
    confidence = dict['confidence']     #get confidence field from tensor flow output
    if confidence >= 0.45: return True
    else: return False
    

