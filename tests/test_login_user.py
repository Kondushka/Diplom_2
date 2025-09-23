import requests
import pytest
import allure
from data.api import Api
from data.response import Response


@allure.suite('Тесты: вход в систему')
@allure.sub_suite("Авторизация ползователя")

class TestLoginUser:
    @allure.title('Авторизация существующего ползователя')
    def test_login_user(self, create_user, user_data, delete_user):
        
        with allure.step('Пытаемся авторизоваться под существующим пользователем'):
            response = requests.post(Api.LOGIN_USER_API, json = user_data, timeout=10)
        
        with allure.step('Авторизация прошла успешно'):
            assert response.status_code == 200
            assert response.json().get("success") == True
            assert Response.TOKEN_ACCESS in response.json()
        
        
    @allure.title('Авторизация с неправильным логином/паролем')
    @pytest.mark.parametrize('login, password,  missing_field', [('123Q@gmail.com', '', 'password'), ('', '123Q', 'email') ])
    def test_create_user_without_data(self, login, password, missing_field):
        user = {
            "email": login, 
            "password": password
        }
        
        with allure.step(f'Авторизация с неправильным: {missing_field}'):
            response = requests.post(Api.LOGIN_USER_API, json = user, timeout=10)

        with allure.step('Ловим ошибку'):
            assert response.status_code == 401
            assert response.json().get("success") == False
            assert response.json().get('message') == Response.MESSAGE_WRONG_LOGIN
    