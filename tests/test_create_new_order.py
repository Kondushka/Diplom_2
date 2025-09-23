import requests
import allure
from data.api import Api
from data.response import Response
from data.ingredient import Ingredients as I

@allure.suite('Тесты: cоздание заказа')
@allure.sub_suite('Создание нового заказа')
class TestCreateOrder:
    
    @allure.title('Попытка создания нового заказа без авторизации и без ингредиентов')
    def test_create_order_without_login_without_ingredients(self):
        response = requests.post(Api.ORDER_API)
        
        with allure.step('Ловим ошибку'):
            assert response.status_code == 400
            assert response.json()['message'] == Response.MESSAGE_NO_INGREDIENT
    
    @allure.title('Попытка создания нового заказа с авторизацией и с ингредиентами')    
    def test_create_order_with_login_with_ingredients(self, user_data, create_user, delete_user):
        
        response = requests.post(Api.ORDER_API, headers = {"Authorization": create_user["access_token"]}, json = {"ingredients": [I.BUN, I.CHEESE]})
        order = response.json()['order']['number']
        owner= response.json()["order"]["owner"]["name"]
        
        with allure.step(f'Заказ создан, номер заказа: {order}, имя клиента: {owner}'):
            assert response.status_code == 200
            assert user_data['name'] in owner
                
        
    @allure.title('Попытка создания нового заказа без авторизации, но с ингредиентами')
    def test_create_order_without_login_with_ingredients(self):
        response = requests.post(Api.ORDER_API, json = {"ingredients": [I.FILLET, I.BUN]})
        order = response.json()['order']["number"]
        
        with allure.step(f'Заказ создан, номер заказа: {order}'):
            assert response.status_code == 200
            
            
    @allure.title('Попытка создания нового заказа с авторизацией и без ингредиентов')    
    def test_create_order_with_login_without_ingredients(self, create_user, delete_user):
        
        response = requests.post(Api.ORDER_API, headers = {"Authorization": create_user["access_token"]})
    
        
        with allure.step('Ловим ошибку'):
            assert response.status_code == 400
            assert response.json()['message'] == Response.MESSAGE_NO_INGREDIENT
            
            
    @allure.title('Попытка создания нового заказа с авторизацией и с некорректными ингредиентами')    
    def test_create_order_with_login_with_wrong_ingredients(self, create_user, delete_user):
        
        response = requests.post(Api.ORDER_API, headers = {"Authorization": create_user["access_token"]}, json = {"ingredients": [I.FALS_BUN]})
        
        with allure.step('Ловим ошибку'):
            assert response.status_code == 400
            assert response.json()['message'] == Response.MESSAGE_FALSE_INGREDIENT
            
    
    @allure.title('Попытка создания нового заказа без авторизации и с некорректными ингредиентами')    
    def test_create_order_without_login_with_wrong_ingredients(self, delete_user):
        
        response = requests.post(Api.ORDER_API, json = {"ingredients": [I.FALS_BUN]})
        
        with allure.step('Ловим ошибку'):
            assert response.status_code == 400
            assert response.json()['message'] == Response.MESSAGE_FALSE_INGREDIENT
            
