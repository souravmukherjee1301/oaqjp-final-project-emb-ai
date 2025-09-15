import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  
    '''Define a function named emotion_detector that takes a string input (text_to_analyse)'''
    # URL of the emotional detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the emotional detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Handle blank input (status 400)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    # Handle internal server error
    if response.status_code == 500:
        return None

    # Normal valid response (200)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        
        # Find dominant emotion
        highest_key = max(emotion, key=emotion.get)
        dominant_dict = {"dominant_emotion": highest_key}
        emotion.update(dominant_dict)
        return emotion

    return None