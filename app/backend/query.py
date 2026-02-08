#search supabase database for if material is recyclable in given zipcode

from supabase import create_client
import os

#connect to supabase database
def connect():

    #store supabase database url and key
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY_ANON")

    #catch error if key or url not found
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables.")

    #create supabase client to connect to database
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase #client




#if recyclable return true
def recyclable(zipcode, material):
    supabase = connect()    #call method to connect to database
    if material == "": return False   #if material is "8-not plastic" return not recyclable
    re_field = material + "_Tons_Recycled"  #title of field that contains recycling data, blank if zipcode does not recycle that material

    #query to get object ID connected to zipcode
    response = (
        supabase.table("Zip_codes") #from Zip_codes table
        .select("OBJECTID")         #get field OBJECTID
        .eq("Zip_Code", zipcode)    #where OBJECTID's zipcode matches given zipcode
        .execute()
    )

    #if zipcode exists make list of object ids that have given zipcode
    if response.data:
        object_ids = [row["OBJECTID"] for row in response.data]
    else: 
        object_ids = []

    #if there are object ids find if material is recyclable in area
    if object_ids:
        #query to get recycling data on material
        mat_response = (
            supabase.table(material)        #from given material's table
            .select(re_field)               #get field with recycling data
            .in_("OBJECTID", object_ids)    #where OBJECTIDs match
            .execute()
        )
        
        values = list(mat_response.data[0].values())    #list of data from query
        if values[0] != None: ifrecyclable = True       #if there is data on recycling material is recyclable, return true
        else: ifrecyclable = False                      #if no data return false

        return ifrecyclable
    #if zipcode is not valid return false
    else: return False

    
