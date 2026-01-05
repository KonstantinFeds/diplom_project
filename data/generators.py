from faker import Faker
import allure

fake = Faker()


def payload_generate_user():
    return {
        "id": fake.random_int(min=1, max=1000),
        "username": fake.user_name()[:20],
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number()[:15],
        "userStatus": fake.random_int(min=0, max=1),
    }

def generate_username():
    return {
        "username": fake.user_name()[:20]
    }


def generate_password():
    return {
        "password": fake.password(length=10)
    }


@allure.step("генерация новых данных для обновления")
def generate_update_payload(old_payload):
    update_payload = payload_generate_user()
    update_payload["id"] = old_payload["id"]
    return update_payload



