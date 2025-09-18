import requests
import pytest
import allure
from data.api import Api
from data.response import Response


@allure.suite('Тесты: регистрация')
@allure.sub_suite("Создание пользователя")

class TestCreatUser:
    @allure.title('Создание нового пользователя')
    def test_create_new_user(self, create_user, delete_user):
        
        with allure.step('Создание нового пользователя прошло успешно'):
            assert create_user['response'].status_code == 200
            assert Response.TOKEN_ACCESS in create_user['response'].json()
            
        
    @allure.title('Создание уже существующего пользователья')
    def test_create_duble_user(self, create_user, user_data, delete_user):
        
        with allure.step('Пытаемся создать существующего пользователя'):
            user = requests.post(Api.CREATE_NEW_USER_API, json = user_data, timeout=10)
        
        
        with allure.step('Ловим ошибку'):
            assert user.status_code == 403
            assert user.json().get('message') == Response.MESSAGE_FALSE_USER
        
        
    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('login, password,  missing_field', [('123@gmail.com', '', 'password'), ('', '123Q', 'email') ])
    def test_create_user_without_data(self, login, password, missing_field):
        user = {
            "email": login, 
            "password": password
        }
        
        with allure.step(f'Пытаемся создать пользователя без обязательного поля: {missing_field}'):
            response = requests.post(Api.CREATE_NEW_USER_API, json = user, timeout=10)

        with allure.step('Ловим ошибку'):
            assert response.status_code == 403
            assert response.json().get('message') == Response.MESSAGE_LOST_INPUT
    