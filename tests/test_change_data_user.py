import requests
import allure
from data.api import Api
from data.response import Response


@allure.suite('Тесты: данные пользователя')
@allure.sub_suite("Изменение данных пользователя")

class TestChangeDataUser:
    
    @allure.title('Изменение почты пользователя с авторизацией')
    def test_change_email_with_login(self, create_user, user_data, change_user_data, delete_user):
        
        with allure.step('Проверяем исходные данные'):
            
            assert create_user["response"].status_code == 200
            assert create_user["response"].json()['user']['email'] == user_data['email']
            
        with allure.step('Успешно меняем почту'):    
            change_email = requests.patch(Api.USER_API, headers = {"Authorization": create_user["access_token"]}, json = {"email": change_user_data['email']}, timeout=10)
            
            assert change_email.status_code == 200
            assert change_email.json()['user']['email'] == change_user_data['email']
        
    
    @allure.title('Изменение имени пользователя с авторизацией')
    def test_change_name_with_login(self, create_user, user_data, change_user_data, delete_user):
        
        with allure.step('Проверяем исходные данные'):
            
            assert create_user["response"].json()['user']['name'] == user_data['name']
            
        with allure.step('Успешно меняем имя'):
        
            change_name = requests.patch(Api.USER_API, headers = {"Authorization": create_user["access_token"]}, json = {"name": change_user_data['name']}, timeout=10)
            assert change_name.status_code == 200
            assert change_name.json()['user']['name'] == change_user_data['name']
        
        
    
    
    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_data_without_login(self, change_user_data):

        with allure.step('Ловим ошибку при попытке изменить данные без авторизации'):
            response = requests.patch(Api.USER_API, json = {"email":change_user_data['email'], "name": change_user_data['name']}, timeout=10)
            assert response.status_code == 401
            assert response.json()['message'] == Response.NO_AUTHORISED
        
            

