import requests
import allure
from data.api import Api
from data.response import Response

@allure.suite('Тесты: получение заказов')
@allure.sub_suite('Получение заказов конкретного пользователя')
class TestAddOrder:
    
    @allure.title('Попытка получения заказов пользователя без авторизации')
    def test_add_order_without_login(self):
        response = requests.get(Api.ORDER_API)
        
        with allure.step('Ловим ошибку'):
            assert response.status_code == 401
            assert response.json()['message'] == Response.NO_AUTHORISED
    
    @allure.title('Получение заказова пользователя  с авторизацией')    
    def test_create_order_with_login_with_ingredients(self, create_user, delete_user):
        
        response = requests.get(Api.ORDER_API, headers = {"Authorization": create_user["access_token"]})
        orders = response.json()['orders']
        
        with allure.step('Проверяем, что список заказов у клиента пустой'):
            assert len(orders) == 0
            
        with allure.step('Добавляем заказ'):
            add_order = requests.post(Api.ORDER_API, headers = {"Authorization": create_user["access_token"]}, json = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]})
            assert add_order.status_code == 200
            
            
        with allure.step('Проверяем, что список заказов у клиента не пустой'):
            response = requests.get(Api.ORDER_API, headers = {"Authorization": create_user["access_token"]})
            list_orders = response.json()['orders']
            assert len(list_orders) == 1
        