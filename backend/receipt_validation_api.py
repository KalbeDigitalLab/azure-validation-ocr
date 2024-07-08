import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

class CustomVisionService:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        
        # Retrieve environment variables
        self.training_endpoint = os.getenv("VISION_TRAINING_ENDPOINT")
        self.training_key = os.getenv("VISION_TRAINING_KEY")
        self.prediction_key = os.getenv("VISION_PREDICTION_KEY")
        self.prediction_endpoint = os.getenv("VISION_PREDICTION_ENDPOINT")
        self.prediction_resource_id = os.getenv("VISION_PREDICTION_RESOURCE_ID")
        self.publish_iteration_name = "classifyModel"
        
        # Setup clients
        self.setup_clients()

    def setup_clients(self):
        training_credentials = ApiKeyCredentials(in_headers={"Training-key": self.training_key})
        self.trainer = CustomVisionTrainingClient(self.training_endpoint, training_credentials)
        
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.prediction_key})
        self.predictor = CustomVisionPredictionClient(self.prediction_endpoint, prediction_credentials)
        
        # Load the first project for simplicity, consider a more robust approach for production
        self.project = self.trainer.get_projects()[0]
        print(f"Project Name: {self.project.name}")

    def classify_image(self, image_path):
        with open(image_path, "rb") as image_contents:
            results = self.predictor.classify_image(
                self.project.id, self.publish_iteration_name, image_contents.read())
            
            # Display the results
            # for prediction in results.predictions:
            #     print(f"\t{prediction.tag_name}: {prediction.probability * 100:.2f}%")
            
            # Initialize variables to track the maximum probability and corresponding tag name
            max_probability = 0
            max_tag_name = ""

            # Iterate through predictions to find the one with the highest probability
            for prediction in results.predictions:
                if prediction.probability > max_probability:
                    max_probability = prediction.probability
                    max_tag_name = prediction.tag_name

            # Print the prediction with the highest probability
            print(f"{max_tag_name}: {max_probability:.2f}%")
            return max_tag_name

# Usage
if __name__ == "__main__":
    cv_service = CustomVisionService()
    cv_service.classify_image("sample_test_data/aeon.jpg")