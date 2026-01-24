#search supabase database for if material is recyclable in given zipcode

#connect to supabase database
def connect():
    from supabase import create_client, Client
    supabase_url = ("https://rfpyabaqxqegzqvbgdia.supabase.co")
    supabase_key = ("sb_publishable_I94_wif2B3U8LJFnGHXpGA_jTcEb3no")
    supabase: Client = create_client(supabase_url, supabase_key)
    return supabase


def recyclable(zipcode, material):
    supabase = connect()    #connect to database
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

zipcode = 72315
print(recyclable(zipcode, "PET_Bottles"))
print(recyclable(zipcode, "PET_Other_Rigid"))
print(recyclable(zipcode, "PP"))
print(recyclable(zipcode, "Paper"))
print(recyclable(zipcode, "Aluminum"))
print(recyclable(zipcode, "Glass"))
print(recyclable(zipcode, "Cardboard_Boxboard"))
print(recyclable(zipcode, "HDPE_Bottles"))
print(recyclable(zipcode, "Rigids__3_to_7"))