from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    order = data.get("order", {})
    total = order.get("totalSumm", 0)
    delivery_str = order.get("customFields", {}).get("dostavka_do")

    if not delivery_str:
        return jsonify({"klassifikatsiya": "UNCLASSIFIED"})

    try:
        delivery_date = datetime.strptime(delivery_str, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"klassifikatsiya": "UNCLASSIFIED"})

    today = datetime.today().date()
    diff_days = (delivery_date - today).days

    if total < 500000 and diff_days > 30:
        return jsonify({"klassifikatsiya": "D"})

    if total > 50000:
        if diff_days in [0, 1]:
            return jsonify({"klassifikatsiya": "AA"})
        elif 1 < diff_days <= 14:
            return jsonify({"klassifikatsiya": "AB"})
        elif diff_days > 14:
            return jsonify({"klassifikatsiya": "AC"})
    elif 20000 <= total <= 50000:
        if diff_days in [0, 1]:
            return jsonify({"klassifikatsiya": "BA"})
        elif 1 < diff_days <= 14:
            return jsonify({"klassifikatsiya": "BB"})
        elif diff_days > 14:
            return jsonify({"klassifikatsiya": "BC"})
    elif total < 20000:
        if diff_days in [0, 1]:
            return jsonify({"klassifikatsiya": "CA"})
        elif 1 < diff_days <= 14:
            return jsonify({"klassifikatsiya": "CB"})
        elif diff_days > 14:
            return jsonify({"klassifikatsiya": "CC"})

    return jsonify({"klassifikatsiya": "UNCLASSIFIED"})
