# import open ai and define the client
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from PIL import Image
import pytesseract
import requests
from io import BytesIO
from dotenv import load_dotenv

import os
load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# extract image from a url
def extractImageText(url):
    imgResponse = requests.get(url, timeout=10)
    img = Image.open(BytesIO(imgResponse.content))
    return pytesseract.image_to_string(img)

# generates the link refering to the local recycling regulations for the adress provided
def generateLink(address):
    stateLinks = {"Cleveland, Ohio": "https://www.cuyahogarecycles.org/recycle-in/cleveland/", "Stanaford, West Virginia" : "https://www.enterprisesanitationinc.com/recycling", "Blytheville, Arkansas" : "https://www.rogersar.gov/1031/Curbside-Recycling-Pickup"}

    return stateLinks[address]



# function that takes info about recyclable and generates short paragraph about why and how to recycle it
def createNotes(address, material, isRecyclable, if_confident):
    url = generateLink(address)

    # generates a response about how to recycle if it is recyclable
    if isRecyclable:
    
        try:
            # get the page at the url
            response = requests.get(url)

            # create a beautiful soup object
            soup = BeautifulSoup(response.content, 'html.parser') 

            # find all the images in the file
            images = soup.find_all("img")

            # sort out unecessary parts of soup
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            # locate keywords --------------------------> IMPORTANT TO UPDATE IF NEEDED
            keywords = ["lids", "lid", "caps", "cap", "wrap", "cardboard", "plastics", "plastic", "#1", "#2", "cannot"]

            # contains found keywords and the text around them
            identifiedInfo = []
            
            # split the text in the beautiful soup file 
            visible_text = soup.get_text(separator=" ")

            # split into the sentences in the page
            sentences = re.split(r'(?<=[.!?])\s+', visible_text)
            

            # find all the keywords in the text
            for key in keywords:
                # finds area around the key as well
                limitKey = r'\b' + re.escape(key) + r'\b'
                for i in range(len(sentences)):
                    sentence = sentences[i]
                    if re.search(limitKey, sentence, flags = re.IGNORECASE):
                        identifiedInfo.append(' '.join(sentences[max(0,i - 3):i + 1]).strip())




            # locate all pdfs in page
            all_pdf_links = soup.find_all('a', href=re.compile(r".+\.pdf$"))

            # wipe the info in pdfText.txt
            open("pdfText.txt", "w").close()

            # scrape the pdfs
            for link in all_pdf_links:
                try:
                    absoluteURL = None
                    href = link.get("href")
                    if href:
                        # create the absolute URL
                        absoluteURL = urljoin(url, href)
                    
                    # retrieves and stores data from the url
                    pdf_response = requests.get(absoluteURL)

                    # extract data from pdf document
                    reader = PdfReader(BytesIO(pdf_response.content))

                    # extract the text and put it in a txt file
                    for page in reader.pages:
                        text = page.extract_text()
                        
                        with open("pdfText.txt", 'a') as f:
                            f.write(text)
                    
                    with open("pdfText.txt", 'a') as f:
                        f.write('\n')

                except Exception as e:
                    print("pdf error:", e)
                

            # search the pdftext file for the keyword
            with open("pdfText.txt", 'r') as file:
                for line in file:
                    print("\n searching file line: " + line)

                    # identify keys
                    for key in keywords:

                        # append info to the identified info list
                        if key.lower() in line.lower():
                            identifiedInfo.append(line)

            # search all images
            for img in images:
                src = img.get("src")
                
                # if the image is not none
                if not src:
                    continue

                # get the image url
                imgURL = urljoin(url, src)

                
                try:
                    # get the text from teh image
                    text = extractImageText(imgURL)

                    # check if the key words are in the text from the image
                    for key in keywords:
                        if key.lower() in text.lower():
                            identifiedInfo.append(text.strip())

                except Exception as e:
                    print("image OCR error:", imgURL)     
                
            
            # response with data from web page
            response = client.responses.create(
                model="gpt-5-nano",

                input=("give me a fiew simple recycling instructions for " + material + " bottle based on the info from " + ', '.join(identifiedInfo))
            
            )

            txt = response.output_text
            if if_confident == False:
                txt = "!Warning! \nImage contents are unclear. Here is the most likely result:\n" + response.output_text


            return txt

        except:
            print("runtime error:", url)

            # response without data from web page
            response = client.responses.create(
                model="gpt-5-nano",

                input=("give me 2 bullet points on recycling instructions for how to prepare " + material + " bottle based on the info in " + address)
            
            )
            
            txt = response.output_text
            if if_confident == False:
                txt = "!Warning! \nImage contents are unclear. Here is the most likely result:\n" + response.output_text


            return txt
    
    else:

        # response if not recyclable
        response = client.responses.create(
            model="gpt-5-nano",

            input=("give me very understandable short paragraph on why" + material + "isn't recyclable, assuming that it isn't recyclable anywhere nearby, and what are some options for reusing it" )
            
        )
            
        txt = response.output_text
        if if_confident == False:
            txt = "!Warning! \nImage contents are unclear. Here is the most likely result:\n" + response.output_text


        return txt
    



    



