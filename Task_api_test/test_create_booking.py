from constant import base_url


class TestBooking:

    def test_create_booking(self, auth_session, booking_data):

        create_new_booking = auth_session.post(f"{base_url}/booking", json = booking_data)
        assert create_new_booking.status_code == 200, "Ошибка при создании бронирования"
        booking_id = create_new_booking.json().get("bookingid")
        assert booking_id is not None, "bookingid не найден в ответе"

        assert create_new_booking.json()["booking"]["firstname"] == booking_data['firstname'], "Имя не совпадает"
        assert create_new_booking.json()["booking"]["totalprice"] == booking_data['totalprice'], "Стоимость не совпадает"

        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронирование не найдено"

        deleted_booking = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронирование не найдено"

        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронирование не удалилось"












