import pytest
import allure
import requests
from data.api import Api
from data.helpers import create_user_data


@pytest.fixture()
def user_data():
    return create_user_data()

@pytest.fixture()
def change_user_data(user_data):
    return {
        "email": f'chance_{user_data["email"]}',
        "password": f'chance_{user_data["password"]}',
        "name": f'chance_{user_data["name"]}'    
    }
    

@pytest.fixture()  
def create_user(user_data):

    with allure.step('Создаем нового пользователя'):
        response = requests.post(Api.CREATE_NEW_USER_API, json = user_data, timeout=10)
                
    with allure.step('Сохраняем токен для удаления'):
        access_token = response.json()["accessToken"]  
        
        return {"response": response, "access_token": access_token}
        
@pytest.fixture()  
def delete_user(create_user):
    yield
    
    with allure.step('Удаляем пользователя'):
        return requests.delete(Api.USER_API, headers={"Authorization": create_user["access_token"]}, timeout=10)

