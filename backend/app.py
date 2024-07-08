from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_api import status
from receipt_validation_api import CustomVisionService
from receipt_ocr_api import ReceiptOCR

import os

app = Flask(__name__)
CORS(app)

# Ensure temporary directory exists
TEMP_DIR = os.path.join(os.getcwd(), "temp")
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route("/api/validate-receipt", methods=["POST"])
def validate_receipt_route():
    # Get the document file from the request
    file = request.files["file"]

    # Save the file to a temporary location
    file_path = os.path.join(TEMP_DIR, file.filename)
    file.save(file_path)

    # Process the receipt
    cv_service = CustomVisionService()
    class_result = cv_service.classify_image(file_path)
    
    if class_result.lower() != "receipt":
        # Clean up the temporary file
        os.remove(file_path)
        
        # Return an error response
        return jsonify({"message": "Invalid receipt"}), status.HTTP_400_BAD_REQUEST
    
    # Process the receipt
    ocr = ReceiptOCR(file_path)
    result = ocr.process_receipt_api()

    # Clean up the temporary file
    os.remove(file_path)
    
    # Return the extracted fields
    return result , status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True)
