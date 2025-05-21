from flask import Flask, request, jsonify
from classifier import classify_lead
from crm_client import edit_order_custom_field, get_order_by_id
from logger import setup_logger
import logging
from config import RETAILCRM_API_KEY as API_KEY, RETAILCRM_API_URL as BASE_URL


setup_logger()
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logging.info(f"Received data: {data}")

    classification = classify_lead(data)
    logging.info(f"Calculated classification: {classification}")

    if classification == 'Unknown':
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

    entity_id = data.get('id')
    success = classify_lead(entity_id, classification)

    if not success:
        return jsonify({'status': 'error', 'message': 'Failed to update CRM'}), 500

    return jsonify({'status': 'ok', 'classification': classification}), 200


if __name__ == '__main__':
    app.run(debug=True)
