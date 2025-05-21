# RetailCRM Lead Classifier 🧠

![Python](https://img.shields.io/badge/python-3.11-blue)
![Platform](https://img.shields.io/badge/platform-Heroku-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Классификатор лидов для RetailCRM на Python. Обрабатывает вебхуки и автоматически проставляет категорию лида (A, B, C, D) на основе суммы заказа и даты доставки.

## 🚀 Функциональность

- Веб-сервер на Flask
- Обработка входящих webhook'ов от RetailCRM
- Классификация по бизнес-правилам:
  - A — сумма > 50000 ₽ и доставка в течение месяца
  - B — сумма > 30000 ₽ и доставка в течение 3 месяцев
  - C — остальные
  - D — доставка позже чем через 3 месяца
- Простая архитектура — легко доработать

## 📦 Установка

```bash
git clone https://github.com/Lavr-18/retailcrm-classifier.git
cd retailcrm-classifier
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
