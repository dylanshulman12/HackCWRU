#search supabase database for if material is recyclable in given zipcode

from supabase import create_client, Client
import os

#connect to supabase database
def connect():
    supabase_url = ("https://rfpyabaqxqegzqvbgdia.supabase.co")
    supabase_key = ("sb_publishable_I94_wif2B3U8LJFnGHXpGA_jTcEb3no")

    
    print("SUPABASE_URL =", repr(os.getenv("SUPABASE_URL")))
    print("SUPABASE_KEY =", repr(os.getenv("SUPABASE_KEY")))

    supabase: Client = create_client(supabase_url, supabase_key)
    return supabase

#if recyclable
def recyclable(zipcode, material):
    supabase = connect()    #connect to database
    if not material: return False   #if material is 8-not plastic return not recyclable
    re_field = material + "_Tons_Recycled"  #field to check for recycling data

    #get object ID connected to zipcode
    response = (
        supabase.table("Zip_codes")
        .select("OBJECTID")
        .eq("Zip_Code", zipcode)
        .execute()
    )

    #if zipcode exists use object id
    if response.data:
        object_ids = [row["OBJECTID"] for row in response.data]
    else: 
        object_ids = []

    #find if pet bottles are recycled in zipcode, go to PET_bottles table
    if object_ids:
        pet_response = (
            supabase.table(material)
            .select(re_field)
            .in_("OBJECTID", object_ids)
            .execute()
        )
        #if material has been recycled
        values = list(pet_response.data[0].values())
        if values[0] != None: ifrecyclable = True
        else: ifrecyclable = False

        return ifrecyclable
    #if zipcode is not valid
    else: return False

    
