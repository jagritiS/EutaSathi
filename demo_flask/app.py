from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("templates/index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    text = data.get("text", "").lower()

    reply_en = "If symptoms continue, please visit the nearest health post."
    reply_np = "लक्षण जारी रहेमा नजिकको स्वास्थ्य चौकीमा जानुहोस्।"
    risk = "green"

    if "fever" in text or "jwaro" or "ज्वरो" in text:
        reply_en = "Fever in a new mother or infant can be dangerous. Please seek medical care immediately."
        reply_np = "नयाँ आमाबा वा शिशुमा ज्वरो खतरनाक हुन सक्छ। तुरुन्त स्वास्थ्य चौकी जानुहोस्।"
        risk = "red"

    if "baby crying" in text:
        print("here ")
        reply_en = "Check feeding, warmth, and diaper. Continuous crying may need medical attention."
        reply_np = "दूध, न्यानोपन र डाइपर जाँच गर्नुहोस्। लगातार रोएमा स्वास्थ्यकर्मीलाई देखाउनुहोस्।"
        risk = "green"

    if "breastfeeding pain" in text or "nipple pain" in text:
        reply_en = "Breastfeeding pain is common, but severe pain or fever needs medical advice."
        reply_np = "स्तनपान गर्दा दुखाइ सामान्य हुन सक्छ, तर धेरै दुखेमा वा ज्वरो आएमा जाँच गराउनुहोस्।"
        risk = "green"

    elif "heavy bleeding" in text or "post delivery bleeding" in text:
        reply_en = "Heavy bleeding after delivery is an emergency. Please go to a hospital immediately."
        reply_np = "सुत्केरीपछि धेरै रक्तस्राव खतरनाक हुन्छ। तुरुन्त अस्पताल जानुहोस्।"
        risk = "red"

    return jsonify({
        "answer_en": reply_en,
        "answer_np": reply_np,
        "risk": risk
    })


if __name__ == "__main__":
    app.run(debug=True)
