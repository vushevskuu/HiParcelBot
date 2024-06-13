def validate_advert(data):
    errors = []
    if not data.get("departure_city"):
        errors.append("Город отправления обязателен")
    if not data.get("destination_city"):
        errors.append("Город назначения обязателен")
    if not data.get("departure_date"):
        errors.append("Дата отправления обязательна")
    return errors

def validate_order(data):
    errors = []
    if not data.get("departure_city"):
        errors.append("Город отправления обязателен")
    if not data.get("destination_city"):
        errors.append("Город назначения обязателен")
    if not data.get("desired_departure_date"):
        errors.append("Желаемая дата отправки обязательна")
    return errors