
import pytest
import requests
from faker import Faker

from Task_api_test.constant import headers, base_url

faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(headers)

    response = requests.post(f"{base_url}/auth", headers=headers, json={"username": "admin", "password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации"

    # логика для извлечения токена из response
    token = response.json().get("token")
    assert token is not None, "В ответе нет токена"

    session.headers.update({"Cookie": f"token = {token}"})
    return session


@pytest.fixture()
def booking_data():
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Cigars"
        }


@pytest.fixture()
def create_booking(auth_session, booking_data):

    create_booking = auth_session.post(f"{base_url}/booking", json=booking_data)
    assert create_booking.status_code == 200, "Ошибка при создании бронирования"

    booking_id = create_booking.json().get("bookingid")
    assert booking_id is not None, "bookingid не найден в ответе"

    return booking_id


@pytest.fixture()
def update_booking_data(booking_data):
    return {
            "firstname" : booking_data["firstname"],
            "lastname" : booking_data["lastname"],
            "totalprice" : booking_data["totalprice"],
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : booking_data["bookingdates"]["checkin"],
                "checkout" : booking_data["bookingdates"]["checkout"]
            },
            "additionalneeds" : "Breakfast"
        }


@pytest.fixture()
def partial_update_booking_data():
    return {
            "totalprice" : faker.random_int(min=100, max=100000),
            "depositpaid": False

        }