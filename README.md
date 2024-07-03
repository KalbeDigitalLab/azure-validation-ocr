# Azure Image Validation and OCR


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
│
├── notebook                 <- Jupyter notebooks for training and inference
│
├── output                   <- OCR output images
│
├── sample_test_data         <- Sample images for testing ML models (classification and OCR)
│
├── .gitignore               <- List of files ignored by git
├── README.md                <- Project documentation
├── receipt_ocr.py           <- Implementation of OCR inference
├── receipt_validation.py    <- Implementation of receipt classification inference
|__ requirements.txt         <- List of packages and dependencies
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
