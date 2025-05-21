from datetime import datetime


def classify_lead(data: dict) -> str:
    total_summ = data.get('totalSumm')
    dostavka_do = data.get('dostavka_do')

    if total_summ is None or dostavka_do is None:
        return 'Unknown'

    try:
        delivery_date = datetime.strptime(dostavka_do, '%Y-%m-%d').date()
    except Exception:
        return 'Unknown'

    today = datetime.today().date()
    delta_days = (delivery_date - today).days

    if total_summ < 500000 and delta_days > 30:
        return 'D'

    if total_summ > 50000:
        if delta_days <= 1:
            return 'AA'
        elif delta_days > 14:
            return 'AC'
        else:
            return 'AB'

    if 20000 <= total_summ <= 50000:
        if delta_days <= 1:
            return 'BA'
        elif delta_days > 14:
            return 'BC'
        else:
            return 'BB'

    if total_summ < 20000:
        if delta_days <= 1:
            return 'CA'
        elif delta_days > 14:
            return 'CC'
        else:
            return 'CB'

    return 'Unknown'
