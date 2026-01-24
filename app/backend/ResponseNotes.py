# import open ai and define the client
from openai import OpenAI
client = OpenAI()

# function that takes info about recyclable and generates short paragraph about why and how to recycle it
def createNotes(isRecyclable, typePlastic, locationData):
    # create a response using gpt 5 nano
    response = client.responses.create(
        model="gpt-5-nano",
        input=("Write a short paragraph about why this item " + isRecyclable + " recyclable because the item is " + typePlastic + " and the user's location is " + locationData + ". Also give clear instructions on next steps.")
    )

    print(response.output_text)


createNotes("is", "PET", "allows recycling PET in Boston")


