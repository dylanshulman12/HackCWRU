#take tensor flow output and change it to database fields

#plastics with resin code
def classify_plastic(material):
    if material == "1_polyethylene_pet":
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
    elif material == "8_no_plastic":
        mat_str = None
    return mat_str

#other items
def classify_other(item):
    if (item == "aluminum_food_cans"
        or item == "aluminum_soda_cans"):
        mat_str = "Aluminum"
    elif (item == "cardboard_boxes"
        or item == "cardboard_packaging"):
        mat_str = "Cardboard_Boxboard"
    elif (item == "clothing"):
        mat_str = "Textiles"
    elif (item == "disposable_plastice_cutlery"
          or item == "plastic_cup_lids"
          or item == "plastic_detergent_bottles"
          or item == "plastic_food_containers"
          or item == "plastic_shopping_bags"
          or item == "plastic_soda_bottles"
          or item == "plastic_straws"
          or item == "plastic_trash_bags"
          or item == "plastic_water_bottles"
          or item == "styrofoam_cups"
          or item == "styrofoam_food_containers"):
        mat_str = "Rigids__3_to_7"
    elif (item == "glass_beverage_bottles"
          or item == "glass_cosmetic_containers"
          or item == "glass_food_jars"):
        mat_str = "Glass"
    elif (item == "magazines"
          or item == "newspaper"
          or item == "office_paper"
          or item == "paper_cups"):
        mat_str = "Paper"
    return mat_str