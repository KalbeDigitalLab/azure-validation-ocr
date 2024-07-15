import os 
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# Load Environment 
load_dotenv()

key  = os.getenv("DOCUMENT_INTELLIGENCE_KEY")
endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")

# documentUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/receipt.png"
file_path = "dataset/receipt_dataset/receipt/receipt_2.jpg"

# Create document anaylsis client 
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# # Analyze document from URL
# poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-receipt", document_url)
# result = poller.result()

# Analyse document from path
with open(file_path, "rb") as document:
    poller = document_analysis_client.begin_analyze_document("prebuilt-receipt", document)
    result = poller.result()

# Process and print results
for idx, receipt in enumerate(result.documents):
    print("--------Analysis of receipt #{}--------".format(idx + 1))
    print("Receipt type: {}".format(receipt.doc_type or "N/A"))
    
    merchant_name = receipt.fields.get("MerchantName")
    if merchant_name:
        print(
            "Merchant Name: {} has confidence: {}".format(
                merchant_name.value, merchant_name.confidence
            )
        )
    
    transaction_date = receipt.fields.get("TransactionDate")
    if transaction_date:
        print(
            "Transaction Date: {} has confidence: {}".format(
                transaction_date.value, transaction_date.confidence
            )
        )
    
    if receipt.fields.get("Items"):
        print("Receipt items:")
        for item_idx, item in enumerate(receipt.fields.get("Items").value):
            print("...Item #{}".format(item_idx + 1))
            
            item_description = item.value.get("Description")
            if item_description:
                print(
                    "......Item Description: {} has confidence: {}".format(
                        item_description.value, item_description.confidence
                    )
                )
            
            item_quantity = item.value.get("Quantity")
            if item_quantity:
                print(
                    "......Item Quantity: {} has confidence: {}".format(
                        item_quantity.value, item_quantity.confidence
                    )
                )
            
            item_price = item.value.get("Price")
            if item_price:
                print(
                    "......Individual Item Price: {} has confidence: {}".format(
                        item_price.value, item_price.confidence
                    )
                )
            
            item_total_price = item.value.get("TotalPrice")
            if item_total_price:
                print(
                    "......Total Item Price: {} has confidence: {}".format(
                        item_total_price.value, item_total_price.confidence
                    )
                )
    
    subtotal = receipt.fields.get("Subtotal")
    if subtotal:
        print(
            "Subtotal: {} has confidence: {}".format(
                subtotal.value, subtotal.confidence
            )
        )
    
    tax = receipt.fields.get("TotalTax")
    if tax:
        print("Total tax: {} has confidence: {}".format(tax.value, tax.confidence))
    
    tip = receipt.fields.get("Tip")
    if tip:
        print("Tip: {} has confidence: {}".format(tip.value, tip.confidence))
    
    total = receipt.fields.get("Total")
    if total:
        print("Total: {} has confidence: {}".format(total.value, total.confidence))
    
    print("--------------------------------------")