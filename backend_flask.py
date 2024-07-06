from flask import Flask, request, jsonify
import os
from receipt_validation import CustomVisionService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and origins


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    
    # Save the file temporarily to pass it to the classifier
    temp_path = os.path.join('temp', file.filename)
    file.save(temp_path)

    # Instantiate CustomVisionService and classify the image
    cv_service = CustomVisionService()
    label, _ = cv_service.classify_image(temp_path)

    # Check if the classified label is "Receipt"
    if label.lower() == "receipt":
        # Move the file from temp to the final location if it's a receipt
        final_path = os.path.join('uploaded_file', file.filename)
        os.rename(temp_path, final_path)
        return 'File uploaded successfully'
    else:
        # Remove the temporary file if it's not a receipt
        os.remove(temp_path)

        return jsonify({'success': False, 'message': 'File is not a receipt'}), 400

    # Save the file to a desired location
    # file.save('uploaded_file/' + file.filename)

    # return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)