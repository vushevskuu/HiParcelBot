from unittest.mock import Mock

# Моки для базовых функций
mock_db_service = Mock()
mock_db_service.get_city_by_name.return_value = {"city_name": "Москва"}
mock_db_service.add_advert.return_value = True
mock_db_service.update_advert.return_value = True
mock_db_service.delete_advert.return_value = True
mock_db_service.add_order.return_value = True
mock_db_service.update_order.return_value = True
mock_db_service.delete_order.return_value = True

mock_validation_service = Mock()
mock_validation_service.validate_advert.return_value = []
mock_validation_service.validate_order.return_value = []