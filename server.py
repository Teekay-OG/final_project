# server.py

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# ✅ ADD THIS ROUTE (fixes 404 on homepage)
@app.route("/")
def home():
    return render_template("index.html")


# ✅ FIXED: allow both GET and POST
@app.route("/detect_emotion", methods=["GET", "POST"])
def detect_emotion_route():
    """
    Handles requests from the user to detect emotions in text.
    Returns a message for display on the front-end.
    Handles blank input gracefully.
    """
    result_message = ""

    # Only process when form is submitted
    if request.method == "POST":
        # Get user input from form
        user_text = request.form.get('text_to_analyse', '').strip()

        # ✅ Handle blank input BEFORE calling API
        if not user_text:
            result_message = "Invalid text! Please try again!"
            return render_template('index.html', result=result_message)

        # Call the emotion detector function
        result = emotion_detector(user_text)

        # ✅ Handle API returning None values
        if not result.get('dominant_emotion'):
            result_message = "Invalid text! Please try again!"
        else:
            # Format the system response message
            result_message = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']}, "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )

    return render_template('index.html', result=result_message)


if __name__ == '__main__':
    app.run(debug=True)