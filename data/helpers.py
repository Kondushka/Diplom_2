from faker import Faker

fake = Faker()
    
def create_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
        }

def chance_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()}