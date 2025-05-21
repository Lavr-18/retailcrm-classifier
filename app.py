from flask import Flask, request, jsonify
from dotenv import load_dotenv
import logging
import os

from classifier import classify_lead
from crm_client import edit_order_custom_field

# Загрузка переменных окружения
load_dotenv()

# Логирование
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)


@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    logging.info(f'Получен запрос: {data}')

    classification = classify_lead(data)
    logging.info(f'Результат классификации: {classification}')

    order_id = data.get('id')
    if not order_id:
        logging.warning("ID заказа не передан в запросе.")
        return jsonify({'error': 'order_id not provided'}), 400

    success = edit_order_custom_field(order_id, 'classification', classification)

    return jsonify({
        'order_id': order_id,
        'classification': classification,
        'updated': success
    })


if __name__ == '__main__':
    app.run(debug=True)
