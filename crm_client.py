import os
import requests
from dotenv import load_dotenv
import logging
from config import RETAILCRM_API_KEY as API_KEY, RETAILCRM_API_URL as BASE_URL


load_dotenv()

logger = logging.getLogger(__name__)


def edit_order_custom_field(order_id: int, field_code: str, value: str) -> bool:
    """
    Обновляет пользовательское поле у заказа.
    """
    url = f"{BASE_URL}/api/v5/orders/{order_id}/edit"
    payload = {
        "apiKey": API_KEY,
        "order": {
            "id": order_id,
            "customFields": {
                field_code: value
            }
        }
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        success = result.get("success", False)

        if success:
            logger.info(f"Успешно обновлена классификация заказа {order_id}: {value}")
        else:
            logger.warning(f"Ошибка при обновлении заказа {order_id}: {result}")
        return success

    except requests.RequestException as e:
        logger.error(f"Сетевая ошибка при обновлении заказа {order_id}: {e}")
        return False


def get_order_by_id(order_id: int) -> dict:
    """
    Получает данные заказа по ID.
    """
    url = f"{BASE_URL}/api/v5/orders/{order_id}"
    params = {"apiKey": API_KEY}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        order = response.json().get("order", {})
        logger.info(f"Получен заказ {order_id}")
        return order
    except requests.RequestException as e:
        logger.error(f"Ошибка при получении заказа {order_id}: {e}")
        return {}
