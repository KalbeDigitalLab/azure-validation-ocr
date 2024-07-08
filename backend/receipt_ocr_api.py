import json
import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from PIL import Image, ImageDraw


class ReceiptOCR:
    def __init__(self, image_path):
        # Load environment variables from .env file
        load_dotenv()

        # Retrieve environment variables
        self.key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")
        self.endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
        self.image_path = image_path

        # Initialize DocumentAnalysisClient
        self.document_analysis_client = DocumentAnalysisClient(
            endpoint=self.endpoint, credential=AzureKeyCredential(self.key)
        )

    def process_receipt(self):
        with open(self.image_path, "rb") as f:
            poller = self.document_analysis_client.begin_analyze_document(
                "prebuilt-receipt", document=f
            )
            result = poller.result()

        # Check if any documents were extracted
        if len(result.documents) > 0:
            document = result.documents[0]  # Get the first document

            print("Receipt Fields:")
            self._print_field(document, "MerchantName", "Merchant Name")
            self._print_field(document, "TransactionDate", "Transaction Date")
            self._print_field(document, "Total", "Total")
            self._print_items(document)

        else:
            print("No receipts were extracted from the image.")

        return result

    def process_receipt_api(self):
        with open(self.image_path, "rb") as f:
            poller = self.document_analysis_client.begin_analyze_document(
                "prebuilt-receipt", document=f
            )
            result = poller.result()

        # Prepare JSON response
        response = {}
        if len(result.documents) > 0:
            document = result.documents[0]  # Get the first document

            response["MerchantName"] = document.fields.get("MerchantName").value if document.fields.get("MerchantName") else None
            response["TransactionDate"] = str(document.fields.get("TransactionDate").value if document.fields.get("TransactionDate") else None)
            response["Total"] = document.fields.get("Total").value if document.fields.get("Total") else None

            items = []
            if document.fields.get("Items"):
                for idx, item in enumerate(document.fields["Items"].value):
                    item_data = {
                        "Description": item.value.get("Description").value if item.value.get("Description") else None,
                        "TotalPrice": item.value.get("TotalPrice").value if item.value.get("TotalPrice") else None
                    }
                    items.append(item_data)
            response["Items"] = items
        else:
            response["error"] = "No receipts were extracted from the image."

        return json.dumps(response, indent=4)

    def display_receipt_with_bounding_boxes(self, result):
        # Open the original image
        image = Image.open(self.image_path)
        draw = ImageDraw.Draw(image)

        # Draw bounding boxes for each word
        for page in result.pages:
            for word in page.words:
                x0, y0 = word.polygon[0].x, word.polygon[0].y
                x1, y1 = word.polygon[2].x, word.polygon[2].y
                draw.rectangle([x0, y0, x1, y1], outline="red", width=2)

        # Ensure the output folder exists
        output_folder = "output"
        os.makedirs(output_folder, exist_ok=True)

        # Save the image with bounding boxes
        output_path = os.path.join(output_folder, os.path.basename(self.image_path).replace(".", "_processed."))
        image.save(output_path)

        print(f"Saved processed image to: {output_path}")

    def _print_field(self, document, field_name, display_name):
        if document.fields.get(field_name):
            print(f"{display_name}: {document.fields[field_name].value}")

    def _print_items(self, document):
        if document.fields.get("Items"):
            print("Items:")
            for idx, item in enumerate(document.fields["Items"].value):
                print(f"  Item {idx + 1}:")
                if item.value.get("Description"):
                    print(f"    Description: {item.value['Description'].value}")
                if item.value.get("TotalPrice"):
                    print(f"    Total Price: {item.value['TotalPrice'].value}")

# Example usage
if __name__ == "__main__":
    image_path = "sample_test_data/aeon.jpg"
    ocr = ReceiptOCR(image_path)
    result = ocr.process_receipt()
    ocr.display_receipt_with_bounding_boxes(result)
    response = ocr.process_receipt_api()
    print(response)
