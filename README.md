<div align="center">

 # **OCR Document Extractor for French PDF Files**

 </div>
 
> This Optical Character Recognition (OCR) system is designed to capture key details, such as names and postal addresses, from PDF documents written in French. The OCR > system is hosted in a frontend Next.js application, enabling users to upload PDF files and receive an Excel file containing the extracted details.
>
> Features
>PDF Upload: Users can upload French-language PDF documents.
>
>Text Extraction: The system uses OCR to extract key features such as names, postal addresses, and other relevant data from the documents.
>
>Excel Export: After extraction, the system provides the extracted information in a downloadable Excel file.
>
>Language Support: Specifically optimized for French-language PDFs.
>
>Requirements
>Before running the project, ensure that you have the following:
>
>Node.js (v14.x or later) - Required for the backend and frontend.
>
>Python (v3.6 or later) - Required for the OCR processing.
>
>Tesseract OCR - The OCR engine used for text extraction from images/PDFs.
>
>Next.js - The frontend framework for the web application.
>
>Pandas - Used for generating the Excel file with the extracted data.
>
Installation
1. Clone the Repository

```bash
git clone https://github.com/your-username/ocr-document-extractor.git
cd ocr-document-extractor
```
2. Install Backend Dependencies (Python)
Make sure you have a virtual environment set up and activate it. Then, install the necessary Python packages.

```bash
pip install -r backend/requirements.txt
```


3. Install Frontend Dependencies (Next.js)
From the root of the project, navigate to the frontend folder and install the required Node.js dependencies.

```bash
cd frontend
npm install
```

4. Set up Tesseract OCR
Install Tesseract: Tesseract is the OCR engine used for text extraction. You can install it via the following commands:

For macOS:
```bash
brew install tesseract
```

For Ubuntu:
```bash
sudo apt install tesseract-ocr
```

For Windows: Download the Tesseract installer from here and follow the instructions.

Ensure that the Tesseract executable is added to your system's PATH.

5. Configure Environment Variables
Create a .env file in the root directory of the project and configure the necessary environment variables:

```bash
NEXT_PUBLIC_TESSERACT_PATH=<path-to-tesseract>
```


Usage
1. Run the Frontend (Next.js Application)
Navigate to the frontend directory and run the following command:
```bash
npm run dev
```

This will start the development server, and you can access the frontend via http://localhost:3000.

2. Upload PDF Documents
Open the frontend application.

Use the file upload feature to upload a PDF document written in French.

The OCR system will process the document and extract key details such as names and postal addresses.

3. Download the Extracted Data
Once the OCR processing is complete, the system will generate an Excel file containing the extracted details. You can download this file directly from the application.

Directory Structure


```plaintext
ocr-document-extractor/
├── backend/
│   ├── ocr.py           # OCR processing script (Python)
│   ├── requirements.txt # Python dependencies
├── frontend/
│   ├── pages/           # Next.js page components
│   ├── public/          # Static assets like images
│   ├── components/      # React components for UI
│   └── package.json     # Frontend dependencies
├── .env                 # Environment variables
├── README.md            # This file
└── LICENSE              # Project license
```


Technologies Used
Next.js: For building the frontend of the web application.

Tesseract OCR: The core engine for text extraction from PDFs.

Pandas: For processing and generating the Excel file with extracted data.

Python: The backend language used for OCR processing.

Node.js: Used for managing frontend dependencies and running the server.

Contributing
Contributions to the project are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

Fork the repository.

``Create a feature branch (git checkout -b feature-branch).``

``Commit your changes (git commit -am 'Add new feature').``

``Push to the branch (git push origin feature-branch).``

``Open a pull request to the main branch.``

License
This project is licensed under the @MIT License - see the LICENSE file for details.
