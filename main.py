import os
from dotenv import load_dotenv
import requests
import re

load_dotenv()


OCR_API_PASSWORD = os.getenv("OCR_API_PASSWORD")
USERNAME = os.getenv('OCR_USERNAME')



requestUrl = 'http://www.ocrwebservice.com/restservices/processDocument?language=french&pagerange=1-5&gettext=true';

def call_ocr_api(file_path):
    files = {
        'file': open(file_path, 'rb')
    }

    response = requests.post(requestUrl, files=files, auth=(USERNAME,OCR_API_PASSWORD))



    if response.status_code == 200:
        # Adjust based on your API's response format
        return response.json()  # or response.text
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    

    #usage

if __name__ == '__main__':
    file_path = 'D:/ocr-dev-site/rapport_complet_officiel_exemple.pdf'
    ocr_result = call_ocr_api(file_path)
    ocr_result = call_ocr_api(file_path)


OCRText = ocr_result.get("OCRText", [])
text = "\n".join(OCRText[0])
print(text)
