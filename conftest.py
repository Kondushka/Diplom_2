import pytest
import allure
import requests
from data.api import Api


@pytest.fixture()
def user_data():
    return {
            "email": "123qtest-data@yandex.ru", 
            "password": "123Q", 
            "name": "123Q"
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

