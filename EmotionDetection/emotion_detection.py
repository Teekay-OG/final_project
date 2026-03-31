# emotion_detection.py

import json

# emotion_detection.py

def emotion_detector(text_to_analyse):
    """
    Mock version of Watson EmotionPredict for offline/testing purposes.
    Returns a sample response with emotions.

    Error Handling:
        - If the input text is empty or None, returns all keys with None values (status_code 400).

    Parameters:
        text_to_analyse (str): The text you want to analyze.

    Returns:
        dict: A dictionary containing emotion scores and dominant emotion.
    """
    # Handle blank input (simulate status_code 400)
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Mock response simulating Watson NLP output
    emotions = {
        "joy": 0.9,
        "sadness": 0.1,
        "anger": 0.0,
        "fear": 0.0,
        "disgust": 0.0
    }

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted dictionary
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }