import json
import requests


from Task_api_test.constant import base_url


class TestGetBookingIds:
    def test_get_booking_ids(self):

        get_booking_ids = requests.get(f"{base_url}/booking")
        assert get_booking_ids.status_code == 200, "Список бронирований не получен"

        assert len(get_booking_ids.text) > 0, "Ответ на запрос пустой"

    def test_get_booking_ids_format(self):

        # Выполнение запроса к API
        get_booking_ids = requests.get(f"{base_url}/booking")

        # Отладочный вывод
        print("Status Code:", get_booking_ids.status_code)
        print("Response Headers:", get_booking_ids.headers)
        print("Response Text:", get_booking_ids.text[:500])  # Ограничиваем вывод текста для удобства

        # Проверка статуса ответа
        assert get_booking_ids.status_code == 200, "Список бронирований не получен"

        # Проверка на HTML-ответ
        if "text/html" in get_booking_ids.headers.get("Content-Type", ""):
            raise AssertionError("Ответ сервера - HTML, а не JSON")

        try:
            # Парсинг ответа как JSON
            response_get_booking_ids = json.loads(get_booking_ids.text)

            # Проверка, что ответ является списком
            assert isinstance(response_get_booking_ids, list), "Ответ не является списком"

            # Проверка структуры каждого элемента списка
            for item in response_get_booking_ids:
                assert isinstance(item, dict), "Элемент списка не является словарем"
                assert "bookingid" in item, "Отсутствует ключ bookingid"
                assert isinstance(item["bookingid"], int), "Значение bookingid должно быть целым числом"

        except json.JSONDecodeError:
            raise AssertionError("Ответ не является валидным JSON")













