import requests

from Task_api_test.conftest import update_booking_data
from constant import base_url, headers


class TestUpdateBooking:

    def test_update_booking(self, auth_session, booking_data, update_booking_data, create_booking):

        update_booking = auth_session.put(f"{base_url}/booking/{create_booking}", headers=headers, json=update_booking_data)
        assert update_booking.status_code == 200, "Ошибка при обновлении бронирования"
        assert update_booking.json()["additionalneeds"] == update_booking_data["additionalneeds"], "Дополнительный запрос клиента не совпадает"
        assert update_booking.json()["additionalneeds"] != booking_data["additionalneeds"], "Дополнительный запрос клиента не обновился"
        assert update_booking.json()["firstname"] == booking_data["firstname"], "Имя клиента обновилось"
        assert update_booking.json()["lastname"] == booking_data["lastname"], "Фамилия клиента обновилось"
        assert update_booking.json()["totalprice"] == booking_data["totalprice"], "Сумма к оплате обновилась"
        assert update_booking.json()["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Дата заезда обновилась"
        assert update_booking.json()["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Дата выезда обновилась"

        deleted_booking = auth_session.delete(f"{base_url}/booking/{create_booking}")
        assert deleted_booking.status_code == 201, "Бронирование не найдено"


    def test_update_booking_none_token(self, booking_data, update_booking_data):

        create_booking = requests.post(f"{base_url}/booking", json = booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании бронирования"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "bookingid не найден в ответе"

        update_booking = requests.put(f"{base_url}/booking/{booking_id}", headers=headers, json = update_booking_data)
        assert update_booking.status_code == 403, "Бронирование обновилось без токена"

        deleted_booking = requests.delete(f"{base_url}/booking/{booking_id}")
        assert deleted_booking.status_code == 403, "Бронирование удалилось без токена"

    def test_update_booking_put_invalid_id(self, booking_data, auth_session):
        invalid_booking_id = 99999999

        update_booking = auth_session.put(f"{base_url}/booking/{invalid_booking_id}", json = booking_data)
        assert update_booking.status_code == 404, "Должен быть код 404 для несуществующего бронирования"

    def test_update_booking_put_empty_body(self, booking_data, auth_session, create_booking):

        update_booking = auth_session.put(f"{base_url}/booking/{create_booking}", json = {})
        assert update_booking.status_code == 400, "Должен быть код 400 при пустом теле запроса"













