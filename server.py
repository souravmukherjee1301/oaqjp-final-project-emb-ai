"""
Flask web server for emotion detection using Watson NLP.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Route: /emotionDetector
    Description:
        Detects emotions in a given text using the emotion_detector function.

    Query Parameters:
        textToAnalyze (str): The input text for emotion detection.

    Returns:
        str: A formatted string with the detected emotions and dominant emotion,
             or an error message if input is invalid.
    """

    text_to_analyse = request.args.get("textToAnalyze")

    # Call emotion detection function
    emotions = emotion_detector(text_to_analyse)

    # Handle invalid or blank input (dominant_emotion None or dict None)
    if emotions is None or emotions.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    if not text_to_analyse:
        return jsonify({"error": "Please provide a 'text' query parameter"}), 400

    # Format response message
    response_msg = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return response_msg

@app.route("/")
def render_index_page():
    """
    Route: /
    Description:
        Renders the home page (index.html) for the web application.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('index.html')
