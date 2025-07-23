from faker import Faker
faker = Faker()

def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password

def generate_registration_data_short_password():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password