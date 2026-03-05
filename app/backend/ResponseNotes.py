def createNotes(material):
    if material == "PET_Bottles":
        txt = "Please rinse the item and replace the lid to recycle!"

    elif material == "PP":
        txt = "Because of food contamination please don't recycle yogurt tubs, butter tubs, or take-out containers!"

    elif material == "Rigids__3_to_7" or material == "HDPE_Bottles":
        txt = "If your plastic item has touched food please don't recycle it unless it was a drink container and in " \
        "that case you can rinse the bottle and replace the lid to recycle! Also never recycle styrofoam please!" \
        
    elif material == "Aluminum":
        txt = "If your item is scrap metal larger than food cans it won't be recyclable here, please submit a " \
        "service request through the Customer Service Center"

    elif material == "Cardboard_Boxboard":
        txt = "Please flatten the cardboard and recycle unless it has food or greese on it. Also don't recycle frozen food " \
        "boxes."

    elif material == "Glass":
        txt = "Please don't recycle drinking glasses, window glass, lab glass, pyrex, ceramic dishes, or broken glass"

    elif material == "Paper":
        txt = "Please don't recycle shredded paper, tissue or paper towels, paper coffee cups, waxed paper, or any paper " \
        "with foil decorations"

    elif material == "Trash":
        txt = "These items are never recyclable, sorry"

    else:
        txt = "Unidentified Obj"

    return txt

