# Azure Image Validation and OCR

"Azure Image Validation and OCR" is a project designed to automate the process of validating and extracting information from document receipts. The project utilizes Azure AI services to classify and perform Optical Character Recognition (OCR) on uploaded images.

### Key Features

1. **Image Validation**:
   - When a user uploads a document, the system first checks if the uploaded file is an image.
   - The image is then classified to determine whether it is a receipt or a non-receipt using Azure AI Custom Vision.

2. **Optical Character Recognition (OCR)**:
   - If the image is classified as a receipt, the process continues with OCR.
   - Azure Document Intelligence is used to extract text and relevant information from the receipt.

### Tools and Technologies

- **Azure AI Custom Vision**: Used for image validation and classification to distinguish between receipt and non-receipt images. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/)
- **Azure Document Intelligence**: Used for OCR to extract text from receipt images. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- **Flask**: A lightweight WSGI web application framework for Python. Flask is used for the backend implementation, handling API requests, processing images, and interacting with Azure AI services. Key features of Flask include its simplicity, flexibility, and ease of use for developing web applications. [Learn more](https://flask.palletsprojects.com/en/3.0.x/)

## Dataset

### Hemlock and Cherry Dataset
The Hemlock and Cherry dataset is used for image classification tasks and consists of images of Hemlock and Cherry trees. This dataset is sourced from Azure Cognitive Search sample images, which can be found [here](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/CustomVision/ImageClassification/Images).

### Receipt and Non-Receipt Dataset
The Receipt and Non-Receipt dataset is used for OCR (Optical Character Recognition) and classification tasks. It contains:

- **Receipt Dataset**: Images of receipts, downloaded from [Kaggle OCR Receipts Text Detection Dataset](https://www.kaggle.com/datasets/trainingdatapro/ocr-receipts-text-detection).
- **Non-Receipt Dataset**: Images of non-receipt items, collected manually from various local sources with random non-receipt images.

Both datasets are stored in the `dataset` directory of the project, with subdirectories for each specific dataset.

## Project Structure
```
├── dataset                   <- Project datasets
│   ├── hemlock_cheery_dataset      <- Hemlock and cherry dataset
│   └── receipt_dataset             <- Receipt dataset
|
├── frontend                  <- Simple frontend implementation
|
├── notebook                  <- Jupyter notebooks for training and inference
│
├── output                    <- OCR output images
│
├── sample_test_data          <- Sample images for testing ML models (classification and OCR)
│
├── .gitignore                <- List of files ignored by git
├── README.md                 <- Project documentation
├── receipt_ocr.py            <- Implementation of OCR inference
├── receipt_validation.py     <- Implementation of receipt classification inference
|__ requirements.txt          <- List of packages and dependencies
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/adhiiisetiawan/azure-validation-ocr.git
   ```
2. Navigate to the project directory:
   ```bash
   cd azure-validation-ocr
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Azure AI Custom Vision
Azure AI Custom Vision is an image recognition service that lets you build, deploy, and improve your own image identifier models. An image identifier applies labels to images, according to their visual characteristics. Each label represents a classification or object. Custom Vision allows you to specify your own labels and train custom models to detect them. You can use Custom Vision through a client library SDK, REST API, or through the Custom Vision web portal (https://customvision.ai/).

### How It Works
The Custom Vision service uses a machine learning algorithm to analyze images for custom features. You submit sets of images that do and don't have the visual characteristics you're looking for. Then you label the images with your own labels (tags) at the time of submission. The algorithm trains to this data and calculates its own accuracy by testing itself on the same images. Once you've trained your model, you can test, retrain, and eventually use it in your image recognition app to classify images or detect objects. You can also export the model for offline use. Please follow this guide for detail explanation (https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/).

### Quickstart 
1. Go to https://www.customvision.ai/ and login with your Azure account.
2. Click settings and write down training resources and prediction resources.
3. Create `.env` file and add this following list to write your key and endpoints from Azure AI Custom Vision
   ```env
   VISION_TRAINING_ENDPOINT="<your-training-endpoint>"
   VISION_TRAINING_KEY=<your-training-key>
   VISION_PREDICTION_ENDPOIN="<your-prediction-endpoint>"
   VISION_PREDICTION_KEY=<your-prediction-key>
   VISION_PREDICTION_RESOURCE_ID="<your-prediction-resources-id>"
   ```
4. Run each cell on jupyter notebook if you want to know flow of training process
5. Run `receipt_validation.py` if you want to do inference trained model.


## Azure Document Intelligence
Azure AI Document Intelligence is a cloud-based Azure AI service that enables you to build intelligent document processing solutions. Massive amounts of data, spanning a wide variety of data types, are stored in forms and documents. Document Intelligence enables you to effectively manage the velocity at which data is collected and processed and is key to improved operations, informed data-driven decisions, and enlightened innovation. Please follow this guide for detail explanation (https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/?view=doc-intel-3.0.0)

### Quickstart
1. Go to your Azure Document intelligence Resources.
2. Choose `Resource Management` and then click on `Keys and Endpoint`
3. Copy `Key 1` and `Endpoint`.
4. Paste in `.env` file like before.
   ```env
   DOCUMENT_INTELLIGENCE_KEY=<your-docs-intelligence-key>
   DOCUMENT_INTELLIGENCE_ENDPOINT="<endpoint>"
   ```
5. Run each cell in notebook Azure Document intelligence
6. Run `receipt_ocr.py` if you want to do inference trained model.

## Web Application Description

The web application consists of a simple yet effective integration of Azure AI services for image validation and OCR. It is built using a Flask backend and a basic frontend with HTML, CSS, and JavaScript. The application is structured to offer the following functionality:

1. **Image Upload and Validation**:
   - Users can upload images through the frontend interface.
   - The backend processes the uploaded images, validating whether the file is an image and determining if it is a receipt or not using Azure AI Custom Vision.

2. **Optical Character Recognition (OCR)**:
   - If the image is classified as a receipt, the backend proceeds with OCR using Azure Document Intelligence.
   - The extracted text and relevant information from the receipt are then made available for review.

3. **User Interface**:
   - The frontend is designed for simplicity and ease of use, providing a clean and intuitive interface for users to interact with the application.

The integration of these services ensures that the application can accurately validate and extract information from receipt images, making it a valuable tool for automating document processing tasks.
 
### Run Web Apps
1. Backend Setup
   - Run Flask application
     ```bash
     python3 backend/wsgi.py
     ```
   - The backend server will start and listen for incoming requests.
3. Frontend Setup
   - Navigate to `frontend` folder
   - Open `index.html` in a web browser. This will allow you to interact with frontend interface.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Acknowledgments
We would like to express our sincere gratitude to the following individuals and resources for their valuable contributions to this project:

- The contributors of the **Hemlock and Cherry Dataset**, sourced from the Azure Cognitive Search sample images.
- The creators of the **Receipt Dataset**, available from the Kaggle OCR Receipts Text Detection Dataset.
- The contributors for this project, who provided essential code components.
