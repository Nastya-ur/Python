from Task_api_test.conftest import partial_update_booking_data
from constant import base_url, headers

class TestPartialUpdateBooking:

    def test_partial_update_booking(self, auth_session, booking_data, partial_update_booking_data, create_booking):

        partial_update_booking = auth_session.patch(f"{base_url}/booking/{create_booking}", headers= headers, json= partial_update_booking_data)
        assert partial_update_booking.status_code == 200, "Ошибка при обновлении бронирования"
        assert partial_update_booking.json()["totalprice"] != booking_data["totalprice"]

    def test_partial_update_booking_empty_body(self, auth_session, booking_data, create_booking):

        partial_update_booking_empty_body = auth_session.patch(f"{base_url}/booking/{create_booking}", headers = headers, json = {})
        assert partial_update_booking_empty_body.status_code == 200, "PATCH с пустым телом должен возвращать код 200"

    def test_partial_update_booking_incorrect_type(self, auth_session, booking_data, create_booking):

        partial_update_booking_incorrect_type = auth_session.patch(f"{base_url}/booking/{create_booking}",headers = headers, json = {"firstname":1234})
        assert partial_update_booking_incorrect_type.status_code == 400, "Должен быть код 400 для некорректного формата данных"

    def test_partial_update_booking_patch_remove_field(self, booking_data, auth_session, create_booking):

        patch_booking = auth_session.patch(f"{base_url}/booking/{create_booking}", json = {"firstname": None})
        assert patch_booking.status_code == 400, "Попытка удалить поле"




