def createNotes(material):
    if material == "PET_Bottles":
        txt = "Please rinse the item and replace the lid to recycle!"

    elif material == "PP":
        txt = "Because of food contamination please don't recycle yogurt tubs, butter tubs, or take-out containers!"

    elif material == "Rigids__3_to_7":
        txt = "If your plastic item has touched food please don't recycle it unless it was a drink container and in " \
        "that case you can rinse the bottle and replace the lid to recycle! Never recycle styrofoam!" \
        
    elif material == "Aluminum":
        txt = "If you item is a can include the lid when you recycle! If your item is scrap metal larger than food cans it won't be recyclable here, please submit a " \
        "service request through the Customer Service Center."

    elif material == "Cardboard_Boxboard":
        txt = "Please flatten the cardboard and recycle unless it has food or grease on it. Also don't recycle frozen food " \
        "boxes."

    elif material == "Glass":
        txt = "Please don't recycle drinking glasses, window glass, lab glass, pyrex, ceramic dishes, or broken glass. " \
        "If your lab has a high volume of lab glass contact sustainability@case.edu."

    elif material == "Paper":
        txt = "Please don't recycle shredded paper, tissue or paper towels, paper coffee cups (sleeves are fine), waxed paper, or any paper " \
        "with significant foil decorations. If you wish to recycle shredded paper, place it in a 'Paper Only' bin that can be found in many academic buildings. " \
        "When recycling notebook paper it is okay to leave the metal spirals attached. "

    else:
        txt = "Unidentified Object. More information is available below. If your object matches this criteria, people at CWRU are encouraged to donate gently used classroom supplies through donation drives " \
        "and partnerships with local organizations. In addition, repairing and reusing objects when possible is another environmentally friendly action to take."
        

    return txt
        

# for other sections to be added later:
# pipette tip boxes: "These cannot be included in campus mixed recycling, but they may be placed in a designated bin in a lab"
# e-waste: "To recycle E-waste, fill out the google form linked below. E-waste that cannot be recycled includes: TVs, household appliances, hazardous waste, items containing liquid mercury, ballasts, light bulbs, and solar panels. For more information refer to https://case.edu/sustainability/sites/default/files/2025-09/4.3-I%20Acceptable%20and%20Non-Acceptable%20Materials%20Revised%20-%202.0.pdf"
#           "Please note that Cannon toner cartridges can be shipped back to Cannon in the box that they came in."
# plastic bags: "Do not put plastic bags or film plastics in mixed recycling, but they can be recycled at many local stores."
# light bulbs: "Please submit a request through the Customer Service Center to dispose of these items."
# batteries: "Alkaline batteries (AA, AAA, C, D) can be disposed in the landfill. For all other batteries, including but not limited to lithium ion, rechargable, and cadmium nickel, please submit a request for pickup through the Customer Service Center."
# hazardous waste: "Please submit a request through the Customer Service Center to dispose of these items."
