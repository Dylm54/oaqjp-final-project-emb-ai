import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers=header)
    formatted_response = json.loads(response.text)
    
    deep_response = formatted_response['emotionPredictions'][0]['emotion']
    
    dominant = ''
    highest = 0
    for key, value in deep_response.items():
        if value > highest:
            highest = value 
            dominant = key 

    emotions = {
        'anger': deep_response['anger'],
        'disgust': deep_response['disgust'],
        'fear': deep_response['fear'],
        'joy': deep_response['joy'],
        'sadness': deep_response['sadness'],
        'dominant_emotion': dominant
    }

    return emotions
