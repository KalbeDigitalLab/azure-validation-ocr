import os 
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential

# Load Environment 
load_dotenv()

key  = os.getenv("DOCUMENT_INTELLIGENCE_KEY")
endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")


document_model_admin_client = DocumentModelAdministrationClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# SAS URL to the labeled receipts in Azure Blob Storage
training_files_sas_url = "https://documentintelligence.ai.azure.com"

# custom model
model_id = "custom-receipt-model"
poller = document_model_admin_client.begin_build_document_model(
    source=training_files_sas_url,
    build_mode="template",
    model_id=model_id,
    description="Custom model for analyzing receipts"
)
model = poller.result()

print(f"Model ID: {model.model_id}")
print(f"Model description: {model.description}")
print(f"Model created on: {model.created_on}")

# To use the model for analyzing new receipts
from azure.ai.formrecognizer import DocumentAnalysisClient

# Initialize the Document Analysis client
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Analyze a new receipt using the trained custom model
receipt_path = "sample_test_data/receipt_test_1.jpg"
with open(receipt_path, "rb") as receipt:
    poller = document_analysis_client.begin_analyze_document(model.model_id, receipt)
    result = poller.result()

# Process and print the result as needed
for document in result.documents:
    print(f"Document type: {document.doc_type}")
    for name, field in document.fields.items():
        print(f"Field '{name}': {field.value} (confidence: {field.confidence})")
