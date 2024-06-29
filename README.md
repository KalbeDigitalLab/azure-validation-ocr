# Azure Image Validation and OCR

## Azure AI Custom Vision
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
4. Done


## Azure Document Intelligence
1. Go to your Azure Document intelligence Resources.
2. Choose `Resource Management` and then click on `Keys and Endpoint`
3. Copy `Key 1` and `Endpoint`.
4. Paste in `.env` file like before.
   ```env
   DOCUMENT_INTELLIGENCE_KEY=<your-docs-intelligence-key>
   DOCUMENT_INTELLIGENCE_ENDPOINT="<endpoint>"
   ```
5. Done
